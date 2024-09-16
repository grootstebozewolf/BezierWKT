# main.py

import math
from antlr4 import InputStream, CommonTokenStream
from wkt_parser.wktLexer import wktLexer
from wkt_parser.wktParser import wktParser
from wkt_visitor import WKTVisitor
import matplotlib.pyplot as plt
import numpy as np

# Helper functions

def cross_product_2d(a, b):
    """Calculate the cross product of two 2D vectors."""
    return a[0] * b[1] - a[1] * b[0]

def dot_product_2d(a, b):
    """Calculate the dot product of two 2D vectors."""
    return a[0] * b[0] + a[1] * b[1]

def vector_subtract(a, b):
    """Subtract vector b from vector a."""
    return [a[0] - b[0], a[1] - b[1]]

def vector_add(a, b):
    """Add vectors a and b."""
    return [a[0] + b[0], a[1] + b[1]]

def vector_scale(a, scalar):
    """Scale vector a by a scalar."""
    return [a[0] * scalar, a[1] * scalar]

def vector_length(a):
    """Calculate the length (magnitude) of vector a."""
    return math.sqrt(a[0] ** 2 + a[1] ** 2)

def compute_circle_center(e, f, g):
    """
    Compute the center and radius of the circle passing through points e, f, g.
    If the points are colinear, return None for center and radius.
    """
    x1, y1 = e
    x2, y2 = f
    x3, y3 = g

    # Calculate the determinant
    D = 2 * ((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))
    if D == 0:
        # Points are colinear; circle cannot be determined
        return None, None

    # Compute intermediate values
    x1_sq = x1 ** 2 + y1 ** 2
    x2_sq = x2 ** 2 + y2 ** 2
    x3_sq = x3 ** 2 + y3 ** 2

    # Calculate center coordinates (h, k)
    h = ((x1_sq - x3_sq) * (y2 - y3) - (x2_sq - x3_sq) * (y1 - y3)) / D
    k = ((x2_sq - x3_sq) * (x1 - x3) - (x1_sq - x3_sq) * (x2 - x3)) / D
    center = [h, k]

    # Compute radius
    radius = vector_length([x1 - h, y1 - k])
    return center, radius

def compute_angle(p, center):
    """Compute the angle (in radians) of point p with respect to center."""
    x, y = vector_subtract(p, center)
    angle = math.atan2(y, x)
    return angle

def normalize_angle(angle):
    """Normalize angle to be between 0 and 2π."""
    return angle % (2 * math.pi)

def determine_arc_direction(e, f, g):
    """Determine the direction of the arc (1 for CCW, -1 for CW)."""
    vec_e_f = vector_subtract(f, e)
    vec_f_g = vector_subtract(g, f)
    orientation = cross_product_2d(vec_e_f, vec_f_g)
    return 1 if orientation > 0 else -1

def compute_total_arc_angle(theta_start, theta_end, direction):
    """Compute the total arc angle based on the direction."""
    delta_theta = theta_end - theta_start
    if direction == 1 and delta_theta < 0:
        delta_theta += 2 * math.pi
    elif direction == -1 and delta_theta > 0:
        delta_theta -= 2 * math.pi
    total_angle = delta_theta * direction
    return total_angle

def decide_number_of_segments(total_angle):
    """Decide the number of Bezier segments based on total angle."""
    angle_fraction = total_angle / (2 * math.pi)
    if angle_fraction > 2 / 3:
        return 3
    elif angle_fraction > 1 / 3:
        return 2
    else:
        return 1

def compute_bezier_arc(center, radius, theta_start, theta_end):
    """
    Compute Bezier control points for an arc from theta_start to theta_end.
    """
    # Ensure delta_theta is positive and in the range [0, pi/2]
    delta_theta = (theta_end - theta_start + 2 * math.pi) % (2 * math.pi)
    if delta_theta > math.pi / 2:
        # If the arc is larger than 90 degrees, we need to split it
        mid_theta = theta_start + delta_theta / 2
        return (compute_bezier_arc(center, radius, theta_start, mid_theta) +
                compute_bezier_arc(center, radius, mid_theta, theta_end))

    # Calculate the factor for control point distance
    k = 4/3 * math.tan(delta_theta/4)

    # Start and end points
    P0 = [center[0] + radius * math.cos(theta_start),
          center[1] + radius * math.sin(theta_start)]
    P3 = [center[0] + radius * math.cos(theta_end),
          center[1] + radius * math.sin(theta_end)]

    # Control points
    P1 = [P0[0] - k * radius * math.sin(theta_start),
          P0[1] + k * radius * math.cos(theta_start)]
    P2 = [P3[0] + k * radius * math.sin(theta_end),
          P3[1] - k * radius * math.cos(theta_end)]

    # Convert points to quaternions
    Q0 = (0.0, P0[0], P0[1], 0.0)
    Q1 = (0.0, P1[0], P1[1], 0.0)
    Q2 = (0.0, P2[0], P2[1], 0.0)
    Q3 = (0.0, P3[0], P3[1], 0.0)

    return [Q0, Q1, Q2, Q3]

def construct_bezier_curves(e, f, g):
    """
    Construct Bezier curves approximating the arc passing through points e, f, g.
    """
    center, radius = compute_circle_center(e, f, g)

    if center is None:
        # Points are colinear; construct linear Bezier curve
        NaN = float('nan')
        Q0 = (0.0, e[0], e[1], 0.0)
        Q3 = (0.0, g[0], g[1], 0.0)
        Q1 = (NaN, NaN, NaN, NaN)
        Q2 = (NaN, NaN, NaN, NaN)
        return [[Q0, Q1, Q2, Q3]]

    # Compute angles
    theta_e = compute_angle(e, center)
    theta_g = compute_angle(g, center)

    # Compute total arc angle
    total_angle = (theta_g - theta_e) % (2 * math.pi)
    if total_angle == 0:
        total_angle = 2 * math.pi  # Full circle

    # Determine number of segments based on arc length
    if total_angle > 4 * math.pi / 3:  # More than 2/3 of a circle
        num_segments = 3
    elif total_angle > 2 * math.pi / 3:  # More than 1/3 of a circle
        num_segments = 2
    else:
        num_segments = 1

    # Compute intermediate angles
    angles = [theta_e + i * total_angle / num_segments for i in range(num_segments + 1)]

    # Compute Bezier curves for each segment
    segments = []
    for i in range(num_segments):
        segment = compute_bezier_arc(center, radius, angles[i], angles[i+1])
        segments.append(segment)

    return segments

def construct_bezier_from_circularstring(points):
    """
    Constructs Bezier curves approximating the arcs defined by a CIRCULARSTRING.
    Args:
        points (list of list): A list of [x, y] coordinates.
    Returns:
        list: A list of Bezier curve control points.
    """
    bezier_curves = []
    if len(points) < 3 or len(points) % 2 == 0:
        raise ValueError("CIRCULARSTRING must have an odd number of points >= 3")
    for i in range(0, len(points) - 2, 2):
        e = points[i]
        f = points[i + 1]
        g = points[i + 2]
        bezier_segments = construct_bezier_curves(e, f, g)
        bezier_curves.extend(bezier_segments)
    return bezier_curves

def parse_wkt(wkt_string):
    input_stream = InputStream(wkt_string)
    lexer = wktLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = wktParser(stream)
    tree = parser.geometry()
    visitor = WKTVisitor()
    result = visitor.visit(tree)
    return result

def generate_bezier_curves_from_wkt(wkt_string):
    geometry_data = parse_wkt(wkt_string)
    if geometry_data['type'] == 'CIRCULARSTRING':
        points = geometry_data['points']
        bezier_curves = []
        for i in range(0, len(points) - 2, 2):
            e = points[i]
            f = points[i + 1]
            g = points[i + 2]
            bezier_segments = construct_bezier_curves(e, f, g)
            bezier_curves.extend(bezier_segments)
        return bezier_curves
    else:
        raise NotImplementedError(f"Geometry type {geometry_data['type']} is not supported.")

def evaluate_bezier_curve(control_points, num_points=100):
    """
    Evaluate points along a cubic Bezier curve defined by control points.
    """
    # Ensure control_points is a list of tuples
    if not isinstance(control_points[0], tuple):
        if len(control_points) == 16:  # Assuming it's a flat list of 16 floats
            control_points = [tuple(control_points[i:i+4]) for i in range(0, 16, 4)]
        else:
            raise ValueError("Unexpected control points format")

    # Extract x and y coordinates
    xs = [pt[1] for pt in control_points]
    ys = [pt[2] for pt in control_points]

    # Check for NaN values (colinear case)
    if any(math.isnan(x) for x in xs) or any(math.isnan(y) for y in ys):
        # Linear Bezier curve (straight line between first and last point)
        return [(control_points[0][1], control_points[0][2]),
                (control_points[3][1], control_points[3][2])]
    else:
        # Cubic Bezier curve
        t_values = np.linspace(0, 1, num_points)
        curve_points = []
        for t in t_values:
            x = (1-t)**3 * xs[0] + 3*(1-t)**2*t * xs[1] + 3*(1-t)*t**2 * xs[2] + t**3 * xs[3]
            y = (1-t)**3 * ys[0] + 3*(1-t)**2*t * ys[1] + 3*(1-t)*t**2 * ys[2] + t**3 * ys[3]
            curve_points.append((x, y))
        return curve_points
    
def plot_bezier_curves(bezier_curves):
    plt.figure(figsize=(8, 6))
    
    for segment_group in bezier_curves:
        if not isinstance(segment_group[0], list):
            segment_group = [segment_group]
        
        for segment in segment_group:
            curve_points = evaluate_bezier_curve(segment)
            xs, ys = zip(*curve_points)
            plt.plot(xs, ys, 'b-', label='Bezier Curve' if 'Bezier Curve' not in plt.gca().get_legend_handles_labels()[1] else "")
            
            control_xs = [pt[1] for pt in segment]
            control_ys = [pt[2] for pt in segment]
            plt.plot(control_xs, control_ys, 'ko--', markersize=4, label='Control Points' if 'Control Points' not in plt.gca().get_legend_handles_labels()[1] else "")
    
    plt.title('Bezier Curve Approximation')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    """
    # Example 1: Non-colinear points
    wkt_input1 = 'CIRCULARSTRING (1 0, 0 1, -1 0)'
    bezier_curves1 = generate_bezier_curves_from_wkt(wkt_input1)
    print("Example 1: Non-colinear points")
    plot_bezier_curves(bezier_curves1)

    # Example 2: Colinear points
    wkt_input2 = 'CIRCULARSTRING (0 0, 1 0, 2 0)'
    bezier_curves2 = generate_bezier_curves_from_wkt(wkt_input2)
    print("Example 2: Colinear points")
    plot_bezier_curves(bezier_curves2)

    # Example 3: Complex arc
    wkt_input3 = 'CIRCULARSTRING(0 0, 1 2.1082, 3 6.3246, 0 7, -3 6.3246, -1 2.1082, 0 0)'
    bezier_curves3 = generate_bezier_curves_from_wkt(wkt_input3)
    print("Example 3: Complex arc")
    plot_bezier_curves(bezier_curves3)
    
    # Example 4: Valid straight line
    wkt_input4 = 'CIRCULARSTRING(1 1, 2 0, 2 0, 2 0, 1 1)'
    bezier_curves4 = generate_bezier_curves_from_wkt(wkt_input4)
    print("Example 4: Valid straight line")
    plot_bezier_curves(bezier_curves4)
    
    # Example 5: Unit circle
    wkt_input5 = 'CIRCULARSTRING(1 0, 0 1, -1 0, 0 -1, 1 0)'
    bezier_curves5 = generate_bezier_curves_from_wkt(wkt_input5)
    print("Example 5: Unit circle")
    plot_bezier_curves(bezier_curves5)

    # Example 6: Real world example with GIS coordinates
    wkt_input6 = 'CIRCULARSTRING(29.8925 40.36667,29.628611 40.015000,29.27528 40.31667)'
    bezier_curves6 = generate_bezier_curves_from_wkt(wkt_input6)
    print("Example 6: Real world example with GIS coordinates")
    plot_bezier_curves(bezier_curves6)
"""
    # Example 7: stretched arc
    wkt_input7 = 'CIRCULARSTRING(1 0, -0.5 0.866025, -0.5 -0.866025)'
    bezier_curves7 = generate_bezier_curves_from_wkt(wkt_input7)
    print("Example 7: Stretched arc")
    plot_bezier_curves(bezier_curves7)