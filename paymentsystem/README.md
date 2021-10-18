# Exercise in Mocking

Start with a class with following signature:

```
  class PaymentService:
    def process_payment(User, PaymentDetails):
	...
```

```
  1. [PaymentService] -> (User, PaymentDetails) -> [Fraud Service]
  2. [Fraud Service] -> (boolean / Exception) -> [PaymentService]
  3. [Payment Gateway] -> (PaymentDetails) -> [PaymentGateway]
```

## Acceptance criteria

* If payment is fraudulent, an exception should be thrown
* Payment should only be sent to payment gateway wheb payment is legit

## Testing approach

* Test drive a working implementation of `PaymentService`
* Write the tests assuming that all the classes are already available
* Do not implement any of the methods in the `FraudService` / `PaymentGateway`.
The methods there should throw the `NotImplementedException` to make sure
mocks are properly used.
