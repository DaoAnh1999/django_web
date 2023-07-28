import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'quiz_game.settings');
django.setup()

# Lesson 4-4: pagination

from loginn.models import Question

Question.objects.create(question='Câu 1: Giải Grand Slam đầu tiên trong năm là giải nào?', A = 'Austrlia mở rộng', B = 'Wimbledon', C = 'Roland Garos', D = 'Mỹ mở rộng', answer = 'Austrlia mở rộng')
Question.objects.create(question='Câu 2: Cùng với Hà Nội T&T (vô địch V-League 2010), CLB nào của Việt Nam tham dự AFC Cup 2011?', A = 'Sông Lam Nghệ An', B = 'SHB Đà Nẵng', C = 'Hoàng Anh Gia Lai', D = 'Becamex Bình Dương', answer = 'SHB Đà Nẵng')
Question.objects.create(question='Câu 3: AFC Asian Cup 2011 được tổ chức tại quốc gia nào?', A = 'Qatar', B = 'Hàn Quốc', C = 'Nhật Bản', D = 'Iraq', answer = 'Qatar')
Question.objects.create(question='Câu 4: Đội nào lên ngôi vô địch AFC Asian Cup 2011 tổ chức tại Qatar?', A = 'Nhật Bản', B = 'Australia', C = 'Hàn Quốc', D = 'Uzbekistan', answer = 'Uzbekistan')
Question.objects.create(question='Câu 5: Ai là nhạc sĩ Việt Nam đầu tiên viết opera với tác phẩm “Cô sao” và sau đó là “Người tạc tượng”?', A = 'Đỗ Nhuận', B = 'Hoàng Vân', C = 'Trần Hoàn', D = 'Trọng Đài', answer = 'Trần Hoàn')
Question.objects.create(question='Câu 6: Sông Bến Hải và sông Thạch Hãn nằm ở tỉnh nào?', A = 'Quảng Bình', B = 'Quảng Ninh', C = 'Quảng Trị', D = 'Quảng Ngãi', answer = 'Quảng Ngãi')
Question.objects.create(question='Câu 7: Trong các cây cầu sau, cầu nào là cầu xoay?', A = 'Cầu Thanh Trì', B = 'Cầu Thị Nại', C = 'Cầu Sông Hàn', D = 'Cầu Cần Thơ', answer = 'Cầu Sông Hàn')
Question.objects.create(question='Câu 8: Đại Ngu là quốc hiệu của triều đại nào?', A = 'Triều Ngô', B = 'Triều Hồ', C = 'Các chúa Nguyễn', D = 'Nhà Tây Sơn', answer = 'Triều Ngô')
Question.objects.create(question='Câu 9: Các vua Hùng đặt quốc hiệu nước ta là gì?', A = 'Văn Lang', B = 'Âu Lạc', C = 'Vạn Xuân', D = 'Đại Việt', answer = 'Văn Lang')
Question.objects.create(question='Câu 10: An Dương Vương đặt quốc hiệu nước ta là gì?', A = 'Âu Lạc', B = 'Vạn Xuân', C = 'Đại Cồ Việt', D = 'Đại Việt', answer = 'Đại Việt')

