# Python-OOP </>
⚡️Kapsülleme \ Encapsulation<br />
Method ya da değişkenlere erişimi kısıtlamak anlamına gelir. Bir sınıftaki değişkenleri özel(private) olarak belirleyerek dış erişimden koruyarak erişim yetkileri belirlenebilir.
Python’da bir değişkeni özel(private) yapmak için başına iki tane alt çizgi eklenir.<br />
'
def __init__(self, name, money, adress):
        self.name=name
        self.__money=money #private değişkenler
        self.adress=adress
'
⚡️Miras \ Inheritance<br />
Bir sınıfın tüm mirasına sahip yeni bir sınıf oluşturmamızı sağlar. Miras alınan üst sınıfa atıfta bulunan super() fonksiyonu, miras aldığımız bir üst sınıfın nitelik ve metotları üzerinde değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi sağlar.

⚡️Soyut Sınıflar \ Abstract Classes<br />
Abstract classlar içerisinde bir veya daha fazla abstract method tanımlaması barındıran classlardır.Abstract method dediğimiz şey ise tanımlı methodların sadece ismi olup içeriği olmaması durumudur.Soyut sınıfları miras olarak alındığında içerisinde ki implemente edilmemiş olan tüm fonksiyonlar implemente edilmek zorundadır.

⚡️Overriding<br />
Miras alınan classta bulunan method ile aynı isimli bir method, alt classta bulunuyor ise bu method çağırıldığı zaman alt classtaki methodu çalıştıracaktır. Bu duruma override etme denmektedir. 

⚡️Polymorphism<br />
Aynı isimli methodun miras alınan classta farklı, diğer alt classlar içerisinde farklı kullanılabilmesini sağlamaktadır. 

