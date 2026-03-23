from django.db import models

class Car(models.Model):
    serial_number = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    colour = models.CharField(max_length=50)
    year = models.IntegerField()
    car_for_sale = models.BooleanField(default=True)

class Customer(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    state_or_province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)

class Salesperson(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=200)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

class Mechanic(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

class Service(models.Model):
    service_name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

class ServiceTicket(models.Model):
    service_ticket_number = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField(blank=True)
    date_returned = models.DateField(null=True, blank=True)

class ServiceMechanic(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

class Parts(models.Model):
    part_number = models.CharField(max_length=200)
    description = models.TextField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

class PartsUsed(models.Model):
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)