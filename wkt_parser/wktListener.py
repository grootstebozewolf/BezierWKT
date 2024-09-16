# Generated from wkt.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .wktParser import wktParser
else:
    from wktParser import wktParser

# This class defines a complete listener for a parse tree produced by wktParser.
class wktListener(ParseTreeListener):

    # Enter a parse tree produced by wktParser#file_.
    def enterFile_(self, ctx:wktParser.File_Context):
        pass

    # Exit a parse tree produced by wktParser#file_.
    def exitFile_(self, ctx:wktParser.File_Context):
        pass


    # Enter a parse tree produced by wktParser#geometryCollection.
    def enterGeometryCollection(self, ctx:wktParser.GeometryCollectionContext):
        pass

    # Exit a parse tree produced by wktParser#geometryCollection.
    def exitGeometryCollection(self, ctx:wktParser.GeometryCollectionContext):
        pass


    # Enter a parse tree produced by wktParser#geometry.
    def enterGeometry(self, ctx:wktParser.GeometryContext):
        pass

    # Exit a parse tree produced by wktParser#geometry.
    def exitGeometry(self, ctx:wktParser.GeometryContext):
        pass


    # Enter a parse tree produced by wktParser#pointGeometry.
    def enterPointGeometry(self, ctx:wktParser.PointGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#pointGeometry.
    def exitPointGeometry(self, ctx:wktParser.PointGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#lineStringGeometry.
    def enterLineStringGeometry(self, ctx:wktParser.LineStringGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#lineStringGeometry.
    def exitLineStringGeometry(self, ctx:wktParser.LineStringGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#polygonGeometry.
    def enterPolygonGeometry(self, ctx:wktParser.PolygonGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#polygonGeometry.
    def exitPolygonGeometry(self, ctx:wktParser.PolygonGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiCurveGeometry.
    def enterMultiCurveGeometry(self, ctx:wktParser.MultiCurveGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiCurveGeometry.
    def exitMultiCurveGeometry(self, ctx:wktParser.MultiCurveGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiSurfaceGeometry.
    def enterMultiSurfaceGeometry(self, ctx:wktParser.MultiSurfaceGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiSurfaceGeometry.
    def exitMultiSurfaceGeometry(self, ctx:wktParser.MultiSurfaceGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#curvePolygonGeometry.
    def enterCurvePolygonGeometry(self, ctx:wktParser.CurvePolygonGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#curvePolygonGeometry.
    def exitCurvePolygonGeometry(self, ctx:wktParser.CurvePolygonGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#compoundCurveGeometry.
    def enterCompoundCurveGeometry(self, ctx:wktParser.CompoundCurveGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#compoundCurveGeometry.
    def exitCompoundCurveGeometry(self, ctx:wktParser.CompoundCurveGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiPointGeometry.
    def enterMultiPointGeometry(self, ctx:wktParser.MultiPointGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiPointGeometry.
    def exitMultiPointGeometry(self, ctx:wktParser.MultiPointGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiLineStringGeometry.
    def enterMultiLineStringGeometry(self, ctx:wktParser.MultiLineStringGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiLineStringGeometry.
    def exitMultiLineStringGeometry(self, ctx:wktParser.MultiLineStringGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiPolygonGeometry.
    def enterMultiPolygonGeometry(self, ctx:wktParser.MultiPolygonGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiPolygonGeometry.
    def exitMultiPolygonGeometry(self, ctx:wktParser.MultiPolygonGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiPolyhedralSurfaceGeometry.
    def enterMultiPolyhedralSurfaceGeometry(self, ctx:wktParser.MultiPolyhedralSurfaceGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiPolyhedralSurfaceGeometry.
    def exitMultiPolyhedralSurfaceGeometry(self, ctx:wktParser.MultiPolyhedralSurfaceGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#multiTinGeometry.
    def enterMultiTinGeometry(self, ctx:wktParser.MultiTinGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#multiTinGeometry.
    def exitMultiTinGeometry(self, ctx:wktParser.MultiTinGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#circularStringGeometry.
    def enterCircularStringGeometry(self, ctx:wktParser.CircularStringGeometryContext):
        pass

    # Exit a parse tree produced by wktParser#circularStringGeometry.
    def exitCircularStringGeometry(self, ctx:wktParser.CircularStringGeometryContext):
        pass


    # Enter a parse tree produced by wktParser#pointOrClosedPoint.
    def enterPointOrClosedPoint(self, ctx:wktParser.PointOrClosedPointContext):
        pass

    # Exit a parse tree produced by wktParser#pointOrClosedPoint.
    def exitPointOrClosedPoint(self, ctx:wktParser.PointOrClosedPointContext):
        pass


    # Enter a parse tree produced by wktParser#polygon.
    def enterPolygon(self, ctx:wktParser.PolygonContext):
        pass

    # Exit a parse tree produced by wktParser#polygon.
    def exitPolygon(self, ctx:wktParser.PolygonContext):
        pass


    # Enter a parse tree produced by wktParser#lineString.
    def enterLineString(self, ctx:wktParser.LineStringContext):
        pass

    # Exit a parse tree produced by wktParser#lineString.
    def exitLineString(self, ctx:wktParser.LineStringContext):
        pass


    # Enter a parse tree produced by wktParser#point.
    def enterPoint(self, ctx:wktParser.PointContext):
        pass

    # Exit a parse tree produced by wktParser#point.
    def exitPoint(self, ctx:wktParser.PointContext):
        pass


    # Enter a parse tree produced by wktParser#name.
    def enterName(self, ctx:wktParser.NameContext):
        pass

    # Exit a parse tree produced by wktParser#name.
    def exitName(self, ctx:wktParser.NameContext):
        pass



del wktParser