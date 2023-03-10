
from rest_framework.test import APITestCase
from auctionapp.models import SellerModel,ProductModel,CustomerModel,BidsModel
from auctionapp.test.TestUtils import TestUtils
class OnlineAuctionAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        SellerModel.objects.create(
        seller_name= "Seller1",
        seller_phone_number= 9485843958,
        seller_email_id= "Seller1@gmail.com",
        seller_address= "Vizag")

        ProductModel.objects.create(
        product_id=1,
        seller_id=1,
        product_name= "Samsung",
        product_description="Samsung is a mobile",
        product_price=25000.00,
        product_quantity=1,
        product_start_bidding_amount=30000.00,
        product_last_date_of_bidding='2022-06-05',
        product_category="Mobiles"
        )

        CustomerModel.objects.create(
        customer_id=2,
        customer_user_name= "Customer2",
        customer_password= "venu123",
        customer_phone_number= 9951849555,
        customer_email_id= "customer2@gmail.com",
        customer_address= "Tirupathi")

        BidsModel.objects.create(
        bid_id= 1,
        bid_amount="32000.00",
        bidding_date='2022-06-01',
        product_id= 1,
        customer_id= 2
        )

    def test_post_request_for_seller_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller/'
        data={
        #"seller_id": 3,
        "seller_name": "Seller2",
        "seller_phone_number": 9885843951,
        "seller_email_id": "Seller2@gmail.com"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("Seller_TestPostRequestForSellerWithInsuffuficientDetails", True, "exception")
            print("Seller_TestPostRequestForSellerWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("Seller_TestPostRequestForSellerWithInsuffuficientDetails", False, "exception")
            print("Seller_TestPostRequestForSellerWithInsuffuficientDetails = Failed")

    def test_get_request_for_all_records_of_seller_with_url_mismatch(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/sellers/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("Seller_TestGetRequestForAllRecordsOfSellerWithUrlMismatch", True, "exception")
            print("Seller_TestGetRequestForAllRecordsOfSellerWithUrlMismatch = Passed")
        else:
            test_obj.yakshaAssert("Seller_TestGetRequestForAllRecordsOfSellerWithUrlMismatch", False, "exception")
            print("Seller_TestGetRequestForAllRecordsOfSellerWithUrlMismatch = Failed")

    def test_get_request_for_non_exist_record_of_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller_id/222/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Seller_TestGetRequestForNonExistRecordOfSeller", True, "exception")
            print("Seller_TestGetRequestForNonExistRecordOfSeller = Passed")
        else:
            test_obj.yakshaAssert("Seller_TestGetRequestForNonExistRecordOfSeller", False, "exception")
            print("Seller_TestGetRequestForNonExistRecordOfSeller = Failed")

    def test_delete_request_of_non_exist_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/seller_id/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Seller_TestDeleteRequestOfNonExistSeller", True, "exception")
            print("Seller_TestDeleteRequestOfNonExistSeller = Passed")
        else:
            test_obj.yakshaAssert("Seller_TestDeleteRequestOfNonExistSeller", False, "exception")
            print("Seller_TestDeleteRequestOfNonExistSeller = Failed")

    def test_post_request_for_product_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product/'
        data={
        "seller_id": 3,
        "product_name": "Samsung",
        "product_description": "Samsung is a mobile",
        "product_price": "25000.00",
        "product_quantity": 1,
        "product_start_bidding_amount": "30000.00"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("Product_TestPostRequestForProductWithInsuffuficientDetails", True, "exception")
            print("Product_TestPostRequestForProductWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("Product_TestPostRequestForProductWithInsuffuficientDetails", False, "exception")
            print("Product_TestPostRequestForProductWithInsuffuficientDetails = Failed")

    def test_delete_request_of_non_exist_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product_id/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Product_TestDeleteRequestOfNonExistProduct", True, "exception")
            print("Product_TestDeleteRequestOfNonExistProduct = Passed")
        else:
            test_obj.yakshaAssert("Product_TestDeleteRequestOfNonExistProduct", False, "exception")
            print("Product_TestDeleteRequestOfNonExistProduct = Failed")

    def test_get_request_for_non_exist_product_by_seller(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/get_products/?seller_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Product_TestGetRequestForNonExistProductsBySeller", True, "exception")
            print("Product_TestGetRequestForNonExistProductsBySeller = Passed")
        else:
            test_obj.yakshaAssert("Product_TestGetRequestForNonExistProductsBySeller", False, "exception")
            print("Product_TestGetRequestForNonExistProductsBySeller = Failed")

    def test_get_request_for_non_exist_bids_by_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products/?product_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Bids_TestGetRequestForNonExistBidsByProduct", True, "exception")
            print("Bids_TestGetRequestForNonExistBidsByProduct = Passed")
        else:
            test_obj.yakshaAssert("Bids_TestGetRequestForNonExistBidsByProduct", False, "exception")
            print("Bids_TestGetRequestForNonExistBidsByProduct = Failed")

#---Customer Functionalities

    def test_get_request_for_non_exist_record_of_product(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/product_id/1111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Product_TestGetRequestForNonExistRecordOfProduct ", True, "exception")
            print("Product_TestGetRequestForNonExistRecordOfProduct  = Passed")
        else:
            test_obj.yakshaAssert("Product_TestGetRequestForNonExistRecordOfProduct ", False, "exception")
            print("Product_TestGetRequestForNonExistRecordOfProduct  = Failed")

    def test_post_request_for_customer_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer/'
        data=    {
        #"customer_id": 1,
        "customer_user_name": "Customer1",
        "customer_password": "venu123",
        "customer_phone_number": 9951849634,
        "customer_email_id": "customer1@gmail.com"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("Customer_TestPostRequestForCustomerWithInsuffuficientDetails", True, "exception")
            print("Customer_TestPostRequestForCustomerWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("Customer_TestPostRequestForCustomerWithInsuffuficientDetails", False, "exception")
            print("Customer_TestPostRequestForCustomerWithInsuffuficientDetails = Failed")

    def test_get_request_for_non_exist_record_of_customer(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer_id/222/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Customer_TestGetRequestForNonExistRecordOfCustomer", True, "exception")
            print("Customer_TestGetRequestForNonExistRecordOfCustomer = Passed")
        else:
            test_obj.yakshaAssert("Customer_TestGetRequestForNonExistRecordOfCustomer", False, "exception")
            print("Customer_TestGetRequestForNonExistRecordOfCustomer = Failed")

    def test_put_request_for_customer_with_insuffuficient_details(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/customer_id/2/'
        data=    {
        "customer_id": 2,
        "customer_user_name": "Customer1",
        "customer_password": "venu123",
        "customer_phone_number": 9951849634
        }
        response=self.client.put(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("Customer_TestPutRequestForCustomerWithInsuffuficientDetails", True, "exception")
            print("Customer_TestPutRequestForCustomerWithInsuffuficientDetails = Passed")
        else:
            test_obj.yakshaAssert("Customer_TestPutRequestForCustomerWithInsuffuficientDetails", False, "exception")
            print("Customer_TestPutRequestForCustomerWithInsuffuficientDetails = Failed")

    def test_post_request_for_bids_with_no_product_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/place_bid/?customer_id=2'
        data=    {
        "bid_id": 1,
        "bid_amount": "32000.00",
        "bidding_date": "2022-06-01",
        "product_id": 1,
        "customer_id": 2
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("Bids_TestPostRequestForBidsWithNoProductId", True, "exception")
            print("Bids_TestPostRequestForBidsWithNoProductId = Passed")
        else:
            test_obj.yakshaAssert("Bids_TestPostRequestForBidsWithNoProductId", False, "exception")
            print("Bids_TestPostRequestForBidsWithNoProductId = Failed")

    def test_get_request_for_bids_by_non_exist_date(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products_by_date/?product_id=1&bidding_date=2000-06-01'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Bids_TestGetRequestForBidsByNonExistDate", True, "exception")
            print("Bids_TestGetRequestForBidsByNonExistDate = Passed")
        else:
            test_obj.yakshaAssert("Bids_TestGetRequestForBidsByNonExistDate", False, "exception")
            print("Bids_TestGetRequestForBidsByNonExistDate = Failed")

    def test_get_request_for_bids_by_non_exist_category(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/list_products_by_category/?customer_id=1'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Customer_TestGetRequestForBidsByNonExistCategory", True, "exception")
            print("Customer_TTestGetRequestForBidsByNonExistCategory = Passed")
        else:
            test_obj.yakshaAssert("Customer_TTestGetRequestForBidsByNonExistCategory", False, "exception")
            print("Customer_TTestGetRequestForBidsByNonExistCategory = Failed")
