import os
import re

TichCuc=["hiệu quả","uy tín","hữu ích","đỉnh","đáng tin cậy","tiện lợi","nhỏ gọn","an tâm","mượt","gọn nhẹ","ngon","độc đáo","hàng chuẩn","hợp lý","sắc nét","xịn xò","phù hợp","hấp dẫn","không thua kém","thoải mái","đỉnh cao","điểm cộng","lý tưởng","ấn tượng","hài lòng",'tốt',"tuyệt vời","tận tình","mỏng nhẹ","mạnh","êm","nhanh", 'thích', 'tuyệt', 'xuất sắc',"đúng hẹn","nhiệt tình", 'nổi bật', 'thiết kế đẹp', 'sang trọng', 'độ bền', 'bền bỉ', 'bền', 'hiện đại', 'tiên tiến', 'ổn', 'ổn định', 'an toàn', 'đa dạng', 'linh hoạt', 'đẹp']
TieuCuc=["vô ích","không thật","delay","chậm","điểm trừ","không hài lòng",'không tốt', 'không thích', 'không được', 'tệ', 'không nổi bật', 'xấu', 'nhanh hỏng', 'không bền', 'nhanh hư', 'dễ bể']

def label_comments(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)

            
            sub_folder = os.path.join(folder_path, file_name.replace('.txt', ''))
            if not os.path.exists(sub_folder):
                os.makedirs(sub_folder)

            
            nes_folder = os.path.join(sub_folder, 'Nes')
            pos_folder = os.path.join(sub_folder, 'Pos')
            neu_folder = os.path.join(sub_folder, 'neutral')
            if not os.path.exists(nes_folder):
                os.makedirs(nes_folder)
            if not os.path.exists(pos_folder):
                os.makedirs(pos_folder)
            if not os.path.exists(neu_folder):
                os.makedirs(neu_folder)
            with open(file_path, 'r', encoding='utf-8') as input_file:
                current_comment = ""
                i = 0
                for line in input_file:
                    line = line.strip() 

                    if line:  # Nếu dòng không trống
                        current_comment += line + "\n"
                    elif current_comment.strip():  
                        output_file_path = None
                        for tu in TichCuc:
                            if tu in current_comment.lower():
                                output_file_path = os.path.join(pos_folder, f'bltc{i+1}.txt')
                        for tu in TieuCuc:
                            if tu in current_comment.lower():
                                output_file_path = os.path.join(nes_folder, f'bltc{i+1}.txt')
                        if output_file_path is None:
                            output_file_path = os.path.join(neu_folder, f'bltc{i}.txt')

                        with open(output_file_path, 'a', encoding='utf-8') as output_file:
                            output_file.write(current_comment)

                        i += 1  
                        current_comment = "" 

                # Xử lý bình luận cuối cùng 
                if current_comment.strip():
                    output_file_path = None
                    for tu in TichCuc:
                        if tu in current_comment:
                            output_file_path = os.path.join(pos_folder, f'bltichcuc{i}.txt')
                    for tu in TieuCuc:
                        if tu in current_comment:
                            output_file_path = os.path.join(nes_folder, f'bltieucuc{i}.txt')
                    if output_file_path is None:
                        output_file_path = os.path.join(neu_folder, f'bltc{i}.txt')

                    with open(output_file_path, 'a', encoding='utf-8') as output_file:
                        output_file.write(current_comment)


folder_path_buoc4 = 'E:\Code\BTL_KPW\Cmt_raw'
label_comments(folder_path_buoc4)
