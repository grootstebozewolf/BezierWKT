# wkt_visitor.py

from wkt_parser.wktParser import wktParser
from wkt_parser.wktVisitor import wktVisitor

class WKTVisitor(wktVisitor):
    def visitGeometry(self, ctx: wktParser.GeometryContext):
        if ctx.circularStringGeometry():
            return self.visitCircularStringGeometry(ctx.circularStringGeometry())
        # Handle other geometry types as needed
        else:
            raise NotImplementedError("Only CIRCULARSTRING geometries are supported in this example.")

    def visitCircularStringGeometry(self, ctx: wktParser.CircularStringGeometryContext):
        points = []
        for point_ctx in ctx.point():
            point = self.visitPoint(point_ctx)
            points.append(point)
        return {'type': 'CIRCULARSTRING', 'points': points}
    
    def visitPoint(self, ctx: wktParser.PointContext):
        coordinates = [float(coord.getText()) for coord in ctx.DECIMAL()]
        return coordinates
