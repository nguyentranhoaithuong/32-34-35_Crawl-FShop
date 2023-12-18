
import os
TichCuc=['tốt',"tuyệt vời","tận tình","mỏng nhẹ","mạnh","êm","nhanh", 'thích', 'tuyệt', 'xuất sắc',"đúng hẹn","nhiệt tình", 'nổi bật', 'thiết kế đẹp', 'sang trọng', 'độ bền', 'bền bỉ', 'bền', 'hiện đại', 'tiên tiến', 'ổn', 'ổn định', 'an toàn', 'đa dạng', 'linh hoạt', 'đẹp',"ưu đãi","đẹp","mượt","nhanh","giá rẻ","nhiệt tình","nên mua", "hoàn hảo","vượt trội","ưng ý","không bám","thuận tiện","mỏng",'gọn',"trơn tru","bắt mắt","hiệu quả","uy tín","hữu ích","đỉnh","đáng tin cậy","tiện lợi","nhỏ gọn","an tâm","mượt","gọn nhẹ","ngon", "độc đáo","hàng chuẩn","hợp lý","sắc nét","xịn xò","phù hợp","hấp dẫn","không thua kém","thoải mái","đỉnh cao","điểm cộng","lý tưởng","ấn tượng","hài lòng","oke"]
TieuCuc=["mồ hôi","vô ích","không thật","delay","chậm","điểm trừ","không hài lòng",'không tốt', 'không thích', 'không được', 'tệ', 'không nổi bật', 'xấu', 'nhanh hỏng', 'không bền', 'nhanh hư', 'dễ bể']
def buoc6(duongdan):
    for file_name in os.listdir(duongdan):
        if file_name.endswith('.txt'):
            file_path = os.path.join(duongdan, file_name)
            sub = os.path.join(duongdan, file_name.replace('.txt', ''))
            if not os.path.exists(sub):
                os.makedirs(sub)
            neg = os.path.join(sub, 'Negative')
            pos = os.path.join(sub, 'Positive')
            neu = os.path.join(sub, 'Neutral')
            if not os.path.exists(neg):
                os.makedirs(neg)
            if not os.path.exists(pos):
                os.makedirs(pos)
            if not os.path.exists(neu):
                os.makedirs(neu)

            with open(file_path, 'r', encoding='utf-8') as input_file:
                binhluan = ""
                i = 0
                for line in input_file:
                    line = line.strip() 
                    if line!="":
                        binhluan += line + "\n"
                    elif line=='' and binhluan!="":  
                        output = None
                        for tu in TichCuc:
                            if tu in binhluan.lower():
                                output = os.path.join(pos, f'blTichCuc{i+1}.txt')
                        for tu in TieuCuc:
                            if tu in binhluan.lower():
                                output = os.path.join(neg, f'blTieuCuc{i+1}.txt')
                        if output is None:
                            output = os.path.join(neu, f'blTrungLap{i}.txt')
                        with open(output, 'w', encoding='utf-8') as output_file:
                            output_file.write(binhluan)
                        i += 1  
                        binhluan = "" 
                
duongdan = 'D:\Khai_pha_web\BaoCao\B5_ChuanHoaCmt'
buoc6(duongdan)
