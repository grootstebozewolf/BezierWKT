Feature: Bezier Curve Construction for Circular Arcs Using Quaternions

  Purpose:
    To generate Bezier curves that approximate circular arcs in the 2D plane using quaternions,
    adhering to specific constraints on the number of Bezier segments based on the arc length.

  Scenario: Constructing Bezier Curve for a Semicircular Arc
    Given a WKT string 'CIRCULARSTRING (1 0, 0 1, -1 0)'
    When I construct the Bezier curve using this WKT string
    Then the circle center should be at (0.0, 0.0) with radius 1.0
    And the arc direction should be counterclockwise
    And the total arc angle should be π radians
    And the algorithm should use 2 Bezier segments
    And the output should be an array of control points in the format [[a, b, c, d], ...]

  Scenario: Constructing Bezier Curve for an Arc Less Than 1/3 of a Circle
    Given a WKT string 'CIRCULARSTRING (1 0, 0.8660254 0.5, 0.5 0.8660254)'
    When I construct the Bezier curve using this WKT string
    Then the circle center should be calculated correctly
    And the algorithm should use 1 Bezier segment
    And generate the appropriate control points

  Scenario: Constructing Continuous Bezier Path Through Multiple Points
    Given a WKT string 'CIRCULARSTRING (1 0, 0 1, -1 0, 0 -1, 1 0)'
    When I construct the Bezier curve using this WKT string
    Then the algorithm should partition the sequence into overlapping triplets
    And construct Bezier curves for each triplet
    And the number of Bezier segments should be correct for each arc
    And the start and end points of each Bezier segment should match the input points
    And output a concatenated array of control points representing the full circle
