def find_prependicular(point_one: tuple, point_two: tuple):
    # first point ; (x1, y1)
    # second point ; (x2, y2)
    # calculates the midpoint between the two input points using the formulas:
    mid_x = (point_one[0] + point_two[0]) / 2
    mid_y = (point_one[1] + point_two[1]) / 2
    # calculate slope
    slope = ((point_one[1] - point_two[1]) / (point_one[0] - point_two[0]))
    # calculate perpendicular slope
    prependicular_slop = -1/(slope)
    # checking for infinity slop
    if point_two[0]-point_one[0] == 0:
        return "we have an infinite slope"
    # checking for 0 slope
    elif point_one[1] - point_two[1] == 0:
        slope = 0
        prependicular_slop = slope
        return ((point_two[0] + point_two[0]) / 2, )

    else:
        # Width from the origin
        h = mid_y - (prependicular_slop * mid_x)
        return prependicular_slop, h


def calculate_rectangle_impact_points(rectangle: tuple, prependicular: tuple):
    # prependicular: (m, h): slope and width from the origin; mX + h ---> calculated befor
    # rectangle: (x, y) from the top rightest

    impacted_points = []

    # Check if the point of impact is within the rectangle's boundaries
    def is_within_bounds(point):
        x, y = point
        return 0 <= x <= rectangle[0] and 0 <= y <= rectangle[1]
    # calculates the y-coordinate of the first possible impact point on the rectangle
    point1_y = rectangle[0] * prependicular[0] + prependicular[1]
    if point1_y <= rectangle[1]:
        point1 = (rectangle[0], point1_y)
        if is_within_bounds(point1):
            impacted_points.append(point1)

    if prependicular[0] != 0:
        # calculate the x-coordinate of the second possible impact point on the rectangle
        point2_x = (rectangle[1] - prependicular[1]) / prependicular[0]
        if point2_x <= rectangle[0]:
            point2 = (point2_x, rectangle[1])
            if is_within_bounds(point2):
                impacted_points.append(point2)

        point3_x = -prependicular[1] / prependicular[0]
        if point3_x <= rectangle[0]:
            point3 = (point3_x, 0)
            if is_within_bounds(point3):
                impacted_points.append(point3)

    if prependicular[1] <= rectangle[1]:
        point4 = (0, prependicular[1])
        if is_within_bounds(point4):
            impacted_points.append(point4)
            # return possible impact points
    return impacted_points


# Calculates the impact point between two lines given in slope-intercept form.
def calculate_impact_point(line1: tuple, line2: tuple):

    # Calculate the x-coordinate of the impact point
    impact_x = (line2[1] - line1[1]) / (line1[0] - line2[0])

    # Calculate the y-coordinate of the impact point
    impact_y = line1[0] * impact_x + line1[1]

    # Return the impact point as a tuple (x, y)
    return impact_x, impact_y


def UserInput():
    """
    Calculates and prints the impact points between perpendicular lines and a rectangle, based on user input.

    User will be prompted to enter the coordinates of the points and the top-left coordinates of the rectangle.
    """
    # Prompt the user to enter the coordinates of the points
    points = []

    num_points = 3  # solve it for 3 points
    for i in range(num_points):
        x = float(input(f"Enter the x-coordinate of point {i+1}: "))
        y = float(input(f"Enter the y-coordinate of point {i+1}: "))
        points.append((x, y))

    # Prompt the user to enter the top-left coordinates of the rectangle
    rect_x = float(
        input("Enter the x-coordinate of the top-left corner of the rectangle: "))
    rect_y = float(
        input("Enter the y-coordinate of the top-left corner of the rectangle: "))
    rectangle = (rect_x, rect_y)

    prependicular = []
    for i in range(len(points)):
        # Calculate the perpendicular line between the current point and the next point
        if i < len(points) - 1:
            prependicular.append(find_prependicular(points[i], points[i + 1]))
        else:
            # If it's the last point, calculate the perpendicular line between the current point and the first point
            prependicular.append(find_prependicular(points[i], points[0]))

    # Calculate the impact point between the first two perpendicular lines
    importans_point = calculate_impact_point(
        prependicular[0], prependicular[1])

    impacts = []
    for x in range(len(prependicular)):
        # Calculate the impact points between the perpendicular line and the rectangle
        impacts.append(calculate_rectangle_impact_points(
            rectangle, prependicular[x]))

    for i in range(len(impacts)):
        thrid_point = (i + 2) % len(impacts)
        for j in range(len(impacts[i])):
            # Compare the distances between the impact points, the perpendicular lines, and a third point
            distance1_1 = ((impacts[i][j][0] - points[thrid_point][0]) **
                           2 + (impacts[i][j][1] - points[thrid_point][1]) ** 2) ** 0.5
            distance1_2 = ((impacts[i][j][0] - points[i][0]) **
                           2 + (impacts[i][j][1] - points[i][1]) ** 2) ** 0.5

            if distance1_1 < distance1_2:
                # Remove the impact point if the distance to the third point is smaller than the distance to the starting point
                impacts[i].pop(j)
                break

    all_points = [importans_point,
                  (0, 0), (0, rectangle[1]), (rectangle[0], 0), rectangle]
    for i in impacts:
        for j in i:
            all_points.append(j)

    print(f'Points --> {all_points}')


# UserInput()
