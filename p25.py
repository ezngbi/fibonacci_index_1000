# ý tưởng:
# em sẽ dùng chuỗi để tính bởi vì chuỗi thì có thể cho được 1000 kí tự chứ không có kiểu dữ liệu nào có 
# được 1000 kí tự hết.
def CongChuoi(val1, val2): # Nhưng bởi vì chuỗi thì không thể cộng cho nhau được nên sẽ phải viết một cái hàm cộng chuỗi ra 
    result = '' #kết quả
    remain = 0 #sô dư bởi vì nếu khi cộng mà vượt quá 10 thì phải nhớ 1 vào số ở hàng tiếp theo
    if(len(val1) != len(val2)): #kiểm tra nếu số có các chữ số khác nhau thì sẽ thêm 0 vào
        for j in range(len(val2) - len(val1)):#ví dụ như 29 + 234 thì sẽ phải viết thành 029 + 234
            val1 = '0' + val1
    for i in range(len(val2)-1, -1, -1):#cho một biến i quét qua tất các chữ số. Ở python thì chuỗi nó được coi như mảng
#ví dụ có string = "abc" thì string[0] = a, string[1] = b, string[2] = c
        TongChuSo = int(val2[i]) + int(val1[i]) + remain #lấy 2 con số 029 và 234 làm ví dụ. 
#đầu tiên lấy 9+4 = 13
        if ((TongChuSo >= 10)): #nếu tổng > 10 thì nhớ 1(lấy 3 nhớ 1) 
            result += (str(TongChuSo % 10))
            remain = 1
        else:
            result+=(str(TongChuSo))
            remain = 0
    if(remain == 1):
        result += str(remain) # cho truong hop neu con so cuoi no vuot qua len(val2)
#ví dụ như 10+91, nếu đúng theo chương trình ở trên thì kết quả sẽ chỉ ra là 01 bởi vì biến i chỉ quét qua số chữ số (ở đây là 2)(dòng 11)
    result = str(SoDaoNguoc(int(result), len(result)))#do cộng từ sau ra trước khiến kết quả sẽ bị ngược so với số đúng nên phải đảo vị trí lại
    return result

def SoDaoNguoc(num, count):
    rev = 0
    for x in range((count - 1), -1, -1):
        rev += ((num % 10)*(10**x))    
        num //= 10  
    return rev

def fibonacci(): #khúc này là hàm fibonacci bình thường, với biến times sẽ là số lần cộng
    times = 1
    val1 = '0'
    val2 = '1'
    while(True):
        times += 1
        tmp = val2
        val2 = CongChuoi(val1, val2) # val2 += val1
        val1 = tmp 
        if(len(val2) == 1000):
            break
    return times 

print(fibonacci())