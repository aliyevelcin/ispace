from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=150, unique=True)
#     surname = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     number = models.IntegerField(unique=True)
#     birth = models.DateField()

#     def __str__(self):
#         return self.name
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')
    description = models.TextField()

    def __str__(self):
        return self.description[:50]
    
class News(models.Model):
    img = models.ImageField(upload_to='news/')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    text = models.TextField()
    description = models.TextField()


    def __str__(self):
        return self.title
    
class Mac(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100)
    chip = models.CharField(max_length=100)
    ssd = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='macs/')
    description = models.TextField()
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='macs', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Ipad(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100)
    chip = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    lineup = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='ipads/')
    description = models.TextField()
    size = models.CharField(max_length=100)
    sim = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=100)
    display_type = models.CharField(max_length=100)
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='ipads', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Iphone(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    playback_time = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    lineup = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='iphones/')
    description = models.TextField()
    size = models.CharField(max_length=100)
    sim = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='iphones', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Watch(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    playback_time = models.CharField(max_length=100)
    case_size = models.CharField(max_length=100)
    band_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='watches/')
    description = models.TextField()
    battery_life = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=100)
    display_type = models.CharField(max_length=100)
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='watches', null=True, blank=True)


    def __str__(self):
        return self.name

class Airpods(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    charging_type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    connectivity = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='airpods/')
    description = models.TextField()
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='airpods', null=True, blank=True)


    def __str__(self):
        return self.name

class Tv_Home(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    storage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100)
    connectivity = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='tv_home/')
    description = models.TextField()
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='tv_home', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Accessories(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='accessories/')
    description = models.TextField()
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='accessories', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Giftcards(models.Model):
    name = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='accessories/')
    description = models.TextField()
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, related_name='giftcards', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Offer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='offers/')

    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=200)
    card_img = models.ImageField(upload_to='stores/')
    card_name = models.CharField(max_length=200)
    distance = models.IntegerField()
    location = models.CharField(max_length=300)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    hours = models.CharField(max_length=20)
    map_embed = models.TextField()

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name
    
class Product_type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name