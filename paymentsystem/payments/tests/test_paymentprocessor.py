import unittest
from unittest.mock import MagicMock, patch

from payments.paymentprocessor import FraudService, PaymentGateway, PaymentService


class User:
    pass


class PaymentDetails:
    pass


user = User()
good_payment = PaymentDetails()
fraud_payment = PaymentDetails()


class PaymentProcessorShould(unittest.TestCase):
    @patch.object(FraudService, "isFraud", return_value=False)
    @patch.object(PaymentGateway, "payWith")
    def test_good_payment(self, paywith, isfraud):
        ps = PaymentService(FraudService(), PaymentGateway())
        ps.processPayment(user, good_payment)

        isfraud.assert_called_once_with(user, good_payment)
        paywith.assert_called_once_with(good_payment)

    @patch.object(FraudService, "isFraud", return_value=True)
    @patch.object(PaymentGateway, "payWith")
    def test_fraud_payment(self, paywith, isfraud):
        ps = PaymentService(FraudService(), PaymentGateway())
        with self.assertRaises(ValueError):
            ps.processPayment(user, fraud_payment)

        isfraud.assert_called_once_with(user, fraud_payment)
        paywith.assert_not_called()


if __name__ == "__main__":
    unittest.main()
