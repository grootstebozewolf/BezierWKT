from behave import given, when, then
import math
import numpy as np
from main import (
    generate_bezier_curves_from_wkt,
    parse_wkt,
    compute_circle_center,
    compute_angle,
    normalize_angle,
    determine_arc_direction,
    compute_total_arc_angle,
    decide_number_of_segments,
    compute_bezier_arc,
)

@given('a WKT string {wkt_string}')
def step_given_wkt_string(context, wkt_string):
    context.wkt_string = wkt_string.strip("'")

@when('I construct the Bezier curve using this WKT string')
def step_when_construct_bezier_from_wkt(context):
    wkt_string = context.wkt_string
    geometry_data = parse_wkt(wkt_string)
    context.geometry_data = geometry_data
    points = geometry_data['points']
    context.points = points

    num_points = len(points)
    if num_points >= 3:
        context.num_triplets = (num_points - 1) // 2
        context.bezier_curves = []
        context.control_points = []
        context.arc_directions = []
        context.total_arc_angles = []
        context.num_bezier_segments = []
        context.circle_centers = []
        context.radii = []
        for i in range(0, num_points - 2, 2):
            e = points[i]
            f = points[i + 1]
            g = points[i + 2]

            center, radius = compute_circle_center(e, f, g)
            context.circle_centers.append(center)
            context.radii.append(radius)

            theta_e = compute_angle(e, center)
            theta_g = compute_angle(g, center)
            direction = determine_arc_direction(e, f, g)
            context.arc_directions.append('counterclockwise' if direction == 1 else 'clockwise')
            theta_e = normalize_angle(theta_e)
            theta_g = normalize_angle(theta_g)
            total_arc_angle = compute_total_arc_angle(theta_e, theta_g, direction)
            context.total_arc_angles.append(total_arc_angle)
            num_segments = decide_number_of_segments(abs(total_arc_angle))
            context.num_bezier_segments.append(num_segments)

            control_points = []
            angles = [theta_e + j * (theta_g - theta_e) / num_segments for j in range(num_segments + 1)]
            for j in range(num_segments):
                theta_start = angles[j]
                theta_end = angles[j + 1]
                segment = compute_bezier_arc(center, radius, theta_start, theta_end)
                control_points.append(segment)
            context.bezier_curves.extend(control_points)
            context.control_points.extend(control_points)
    else:
        # Not enough points to construct a Bezier curve
        raise ValueError("Not enough points to construct a Bezier curve")

@then('the circle center should be at ({x:f}, {y:f}) with radius {r:f}')
def step_then_circle_center(context, x, y, r):
    expected_center = (x, y)
    expected_radius = r
    center = context.circle_centers[0]
    radius = context.radii[0]
    assert math.isclose(center[0], expected_center[0], rel_tol=1e-5) and \
           math.isclose(center[1], expected_center[1], rel_tol=1e-5), \
           f"Expected center at {expected_center}, got {center}"
    assert math.isclose(radius, expected_radius, rel_tol=1e-5), \
           f"Expected radius {expected_radius}, got {radius}"

@then('the circle center should be calculated correctly')
def step_then_circle_center_calculated(context):
    for center, radius in zip(context.circle_centers, context.radii):
        assert center is not None, "Circle center not calculated"
        assert radius is not None, "Radius not calculated"

@then('the arc direction should be {direction}')
def step_then_arc_direction(context, direction):
    actual_direction = context.arc_directions[0]
    assert actual_direction == direction, \
        f"Expected {direction}, got {actual_direction}"

@then('the total arc angle should be π radians')
def step_then_total_arc_angle(context):
    expected_angle = math.pi
    total_angle = context.total_arc_angles[0]
    assert math.isclose(total_angle, expected_angle, rel_tol=1e-5), \
        f"Expected angle {expected_angle}, got {total_angle}"

@then('the algorithm should use {n:d} Bezier segments')
def step_then_num_bezier_segments(context, n):
    total_segments = sum(context.num_bezier_segments)
    assert total_segments == n, \
        f"Expected {n} Bezier segments, got {total_segments}"

@then('the algorithm should use {n:d} Bezier segment')
def step_then_num_bezier_segment_singular(context, n):
    total_segments = sum(context.num_bezier_segments)
    assert total_segments == n, \
        f"Expected {n} Bezier segment, got {total_segments}"

@then('generate the appropriate control points')
def step_then_generate_control_points(context):
    assert context.control_points is not None, "Control points not generated"
    for segment in context.control_points:
        assert len(segment) == 4, "Each segment should have 4 control points"

@then('the output should be an array of control points in the format [[a, b, c, d], ...]')
def step_then_output_control_points(context):
    assert isinstance(context.control_points, list), "Control points should be a list"
    for segment in context.control_points:
        assert len(segment) == 4, "Each segment should have 4 control points"

@then('the algorithm should partition the sequence into overlapping triplets')
def step_then_partition_sequence(context):
    expected_triplets = (len(context.points) - 1) // 2
    assert context.num_triplets == expected_triplets, \
        f"Expected {expected_triplets} triplets, got {context.num_triplets}"

@then('construct Bezier curves for each triplet')
def step_then_construct_bezier_for_triplets(context):
    assert len(context.bezier_curves) > 0, "No Bezier curves constructed"

@then('ensure continuity between segments')
def step_then_ensure_continuity(context):
    # Verify that the end point of one segment matches the start point of the next
    for i in range(len(context.control_points) - 1):
        end_point = context.control_points[i][3]
        start_point = context.control_points[i + 1][0]
        assert end_point == start_point, "Segments are not continuous"

@then('output a concatenated array of control points representing the full circle')
def step_then_output_concatenated_control_points(context):
    assert context.control_points is not None, "Full control points not generated"
    assert len(context.control_points) == sum(context.num_bezier_segments), \
        "Number of control point sets doesn't match total number of segments"
    
@then('the number of Bezier segments should be correct for each arc')
def step_then_correct_number_of_segments(context):
    bezier_curves = context.bezier_curves
    input_points = context.points
    
    # For a full circle, we expect 4 segments
    if input_points[0] == input_points[-1] and len(input_points) > 3:
        assert len(bezier_curves) == 4, f"Expected 4 Bezier segments for a full circle, but got {len(bezier_curves)}"
    else:
        # For partial arcs, the number of segments depends on the arc length
        num_arcs = (len(input_points) - 1) // 2
        total_segments = sum(len(arc) for arc in bezier_curves)
        assert total_segments >= num_arcs, f"Expected at least {num_arcs} Bezier segments, but got {total_segments}"

@then('the start and end points of each Bezier segment should match the input points')
def step_then_match_input_points(context):
    input_points = context.points
    bezier_curves = context.bezier_curves
    tolerance = 1e-6  # Define a small tolerance for floating-point comparisons
    
    # Check if it's a full circle
    is_full_circle = input_points[0] == input_points[-1] and len(input_points) > 3
    
    # Check start point
    start_point = bezier_curves[0][0][1:3]
    assert math.isclose(start_point[0], input_points[0][0], rel_tol=tolerance) and \
           math.isclose(start_point[1], input_points[0][1], rel_tol=tolerance), \
           "Start point of the curve doesn't match the first input point"
    
    # Check end point
    end_point = bezier_curves[-1][3][1:3]
    if is_full_circle:
        # For full circles, check if the end point matches the start point
        assert math.isclose(end_point[0], input_points[0][0], rel_tol=tolerance) and \
               math.isclose(end_point[1], input_points[0][1], rel_tol=tolerance), \
               "End point of the curve doesn't match the start point for a full circle"
    else:
        # For partial arcs, check if end point matches the last input point
        assert math.isclose(end_point[0], input_points[-1][0], rel_tol=tolerance) and \
               math.isclose(end_point[1], input_points[-1][1], rel_tol=tolerance), \
               "End point of the curve doesn't match the last input point"
    
    # Check if middle points are approximately on the circle
    for i in range(1, len(input_points) - 1, 2):
        mid_point = input_points[i]
        center, radius = compute_circle_center(input_points[i-1], mid_point, input_points[i+1])
        
        # Find the closest point on any Bezier curve to this mid_point
        closest_distance = float('inf')
        for curve in bezier_curves:
            for point in curve:
                distance = math.sqrt((point[1] - mid_point[0])**2 + (point[2] - mid_point[1])**2)
                closest_distance = min(closest_distance, distance)
        
        # Check if the closest point is approximately on the circle
        assert math.isclose(closest_distance, radius, rel_tol=1e-2), \
               f"Middle point {mid_point} is not approximately on the circle"

    # For full circles, check if we have 4 segments
    if is_full_circle:
        assert len(bezier_curves) == 4, f"Expected 4 Bezier segments for a full circle, but got {len(bezier_curves)}"