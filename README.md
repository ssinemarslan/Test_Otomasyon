Pytest Decatorler 
Pytest, Python programları için bir test çerçevesidir. Yazılım projelerinde testlerin yazılması ve çalıştırılması için kullanılır. 
Pytest, basit test senaryolarından karmaşık test süitlerine kadar çeşitli testleri destekler.
Dekoratörler, pytest test çerçevesini daha esnek ve güçlü kılan özelliklerden sadece birkaç tanesidir.
 Her dekoratörün belirli bir kullanım amacı vardır ve belirli durumlar için test yazımını kolaylaştırmak için tasarlanmıştır.
1-)@pytest.fixture: Test fonksiyonları arasında veri veya durum paylaşmak için kullanılır.
Bir fonksiyonu bir fixture olarak işaretlemek için bu decatorler kullanılır.
2-)@pytest.mark.parametrize: Bir test fonksiyonunu farklı parametre setleriyle çalıştırmak için kullanılır.
3-)@pytest.mark.skip ve @pytest.mark.skipif:Bir testin çalıştırılmasını geçici olarak atlamak veya belirli koşullara bağlı olarak atlamak için kullanılır.
4-)@pytest.mark.xfail : Bir testin bilinçli olarak başarısız olmasını beklediğinizi belirtmek için kullanılır.
