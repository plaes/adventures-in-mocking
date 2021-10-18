class PaymentService:
    def __init__(self, fraudservice, paymentgateway):
        # Injected services
        self.fraudservice = fraudservice
        self.paymentgateway = paymentgateway

    def processPayment(self, user, paymentdetails):
        if self.fraudservice.isFraud(user, paymentdetails):
            raise ValueError
        self.paymentgateway.payWith(paymentdetails)


class FraudService:
    def isFraud(self, user, paymentdetails):
        raise NotImplemented


class PaymentGateway:
    def payWith(self, paymentdetails):
        raise NotImplemented
