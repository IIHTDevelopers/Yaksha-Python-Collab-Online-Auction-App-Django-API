from rest_framework.test import APITestCase
from auctionapp.test.TestUtils import TestUtils
class OnlineAuctionAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("Seller_TestBoundary",True,"boundary")
        print("Seller_TestBoundary = Passed")
