# Generated from wkt.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .wktParser import wktParser
else:
    from wktParser import wktParser

# This class defines a complete generic visitor for a parse tree produced by wktParser.

class wktVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by wktParser#file_.
    def visitFile_(self, ctx:wktParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#geometryCollection.
    def visitGeometryCollection(self, ctx:wktParser.GeometryCollectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#geometry.
    def visitGeometry(self, ctx:wktParser.GeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#pointGeometry.
    def visitPointGeometry(self, ctx:wktParser.PointGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#lineStringGeometry.
    def visitLineStringGeometry(self, ctx:wktParser.LineStringGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#polygonGeometry.
    def visitPolygonGeometry(self, ctx:wktParser.PolygonGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiCurveGeometry.
    def visitMultiCurveGeometry(self, ctx:wktParser.MultiCurveGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiSurfaceGeometry.
    def visitMultiSurfaceGeometry(self, ctx:wktParser.MultiSurfaceGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#curvePolygonGeometry.
    def visitCurvePolygonGeometry(self, ctx:wktParser.CurvePolygonGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#compoundCurveGeometry.
    def visitCompoundCurveGeometry(self, ctx:wktParser.CompoundCurveGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiPointGeometry.
    def visitMultiPointGeometry(self, ctx:wktParser.MultiPointGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiLineStringGeometry.
    def visitMultiLineStringGeometry(self, ctx:wktParser.MultiLineStringGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiPolygonGeometry.
    def visitMultiPolygonGeometry(self, ctx:wktParser.MultiPolygonGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiPolyhedralSurfaceGeometry.
    def visitMultiPolyhedralSurfaceGeometry(self, ctx:wktParser.MultiPolyhedralSurfaceGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#multiTinGeometry.
    def visitMultiTinGeometry(self, ctx:wktParser.MultiTinGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#circularStringGeometry.
    def visitCircularStringGeometry(self, ctx:wktParser.CircularStringGeometryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#pointOrClosedPoint.
    def visitPointOrClosedPoint(self, ctx:wktParser.PointOrClosedPointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#polygon.
    def visitPolygon(self, ctx:wktParser.PolygonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#lineString.
    def visitLineString(self, ctx:wktParser.LineStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#point.
    def visitPoint(self, ctx:wktParser.PointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wktParser#name.
    def visitName(self, ctx:wktParser.NameContext):
        return self.visitChildren(ctx)



del wktParser