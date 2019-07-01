---
## Cài đặt Conda và cách sử dụng :)

---
**Tại sao ta lại cần conda?**

- Trước hết thì Conda là một package manager và enviroment manager được viết bằng python và có thể dùng cho nhiều ngôn ngữ khác nhau. Nó có thể:

- Tạo và quản lý các môi trường.
Tìm kiếm và cài đặt packages vào một môi trường có sẵn Ok tại sao ta cần conda
- Ví dụ như trong quá trình làm việc một dự án cũ, đương nhiên các phiên bản package mà nó sử dụng sẽ cũ luôn theo. Mà những package cũ thì thường sẽ có chút khác biệt với những phiên bản mới hơn. Để làm việc thì ta phải cài đặt lại môi trường hoàn toàn tương thích. Giờ sao chẳng lẽ máy đang python 3.x cài xuống python 2.x rồi còn các project khác. Và conda xuất hiện như một vị anh hùng. Nó cho phép ta tạo một môi trường riêng biệt độc lập với máy chính và độc lập luôn với các môi trường khác.
- Giống như nhà có hai cái phòng, đêm đến một thằng học bài một thằng hát karaoke mà không ảnh hưởng gì tới nhau ý.

https://github.com/phamhongnhung2501/image/blob/master/demo_conda.png


**NOTE:**
- Tác dụng của conda là giới hạn lại các version của các python package mà chúng tương thích với nhau. Ví dụ như cài một package A ở version X thì chỉ có các package B ở version Y1, Y2, Y3 tương ứng có thể cài được. Package B ở version Y5 có conflict nên sẽ không nằm trong kho của conda. Tương tự vậy.


**-Anaconda và Miniconda:**

- Về điểm giống nhau, khi cài đặt thì sẽ cài đặt conda và môi trường gốc base. Anaconda là một một thư viện (em không biết phải dùng từ gì nữa) chứa hơn 720 các package được conda hỗ trợ. Còn Minicoda là một bản rút gọn của Anaconda. Khi cài đặt à không phải nói là để cài đặt được conda ta phải cài đặt một trong hai cái trên. Em đang bước đầu tìm hiểu nên chọn Anacoda cho nó nhiều.

**- Các việc mà Conda làm sẽ như sau :**

- Conda sẽ kiểm tra các channels trong file .condarc (theo thứ tự ưu tiên)
- Sau đó nó sẽ truy cập tới các Repo liên kết có trong channels
- Tìm kiếm trong Repo có chưa package cần hay không nếu không có thể không thể cài đặt được.
- Nếu có 1 package thì conda sẽ tiến hành tải xuống và cái đặt. Còn nếu nó cần thêm vài package nữa để hoạt động thì conda sẽ kiểm tra lại xem có thể cài hết cái đám đó hay không. Nếu không thể cài thì thì package mình cần cũng không được cài luôn. Cho dù chỉ một cái package phụ không cài đặt được.

**- Chanel ???:**
- Channels là những đường link chứa lên kết đển những Storages(những nơi chứa các packages)
https://github.com/phamhongnhung2501/image/blob/master/chanel.png

- Vậy ta có thể lấy các package từ nhiều nơi khác nhau. Không sợ thiếu!
Khoan! nếu mà 1 package cùng có chứa ở 2 nơi thì sao? Lúc này, channels nào được ưu tiên hơn thì sẽ được cài đặt cho dù ở package ở phiên bản nào đi nữa.



**-Download: yêu cầu có sẵn python trên hệ thống:**

- Version 3 dựa trên python3:

```
wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget -c http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86.sh
```

- Chuyển đến thư mục vừa tải nó về và chạy:

```
bash Miniconda2-latest-Linux-x86_64.sh
yes hoặc no (nếu muốn thay đổi folder cài đặt thì gõ vào)
enter thêm phát để đồng ý thêm path vào ~/.bashrc 
 
gõ lệnh: source ~/.bashrc   (để kích hoạt )
```
- Kiểm tra 
```
conda -h
conda -V
```
**- Hướng dẫn tạo môi trường trong python:**
- Cài đặt Conda:
```
conda --version
conda update conda
```

- Tạo môi trường ảo trong Conda:
```
conda create -n myenv                   (Mặc định python giống hiện tại)
conda create -n myenv python=3.4        (Cấu hình python riêng biệt)
conda create -n myenv scipy             (Cấu hình với package _)
conda create -n myenv scipy=0.15.0
```

- Sau đó cài đặt các package:
```
conda install -n myenv scipy
conda install -n myenv scipy=0.15.0    (Khuyến khích ko nên làm thế này, Nên install cùng lúc hết những cái cần)
```

**NOTE:**

– Nếu vậy mỗi khi tạo môi trường mới lại cần install hết lại 1 đống, rất mất thời gian và phải ghi nhớ tên chúng.

=> Ta dùng default, khi nào tạo mt mới, nó tự động cài những thằng default này.

Thêm các package vào phần create_default_packages trong file: .condarc

– Nếu ko muốn dùng default package đối với mt đặc biệt nào đấy thì dùng:
```
conda create –no-default-packages -n myenv python
```
**- Cách tao môi trường từ file: enviroment.yml:**

```
conda env create -f environment.yml (nhớ là dòng đầu tiên trong file này là tên của env)

```

**- Tạo bản clone env:**

```
conda create –name myclone –clone myenv

```
**- Kích hoạt, kiểm tra, hủy kích hoạt:**
- Kích hoạt env bằng cách:
```
source activate myenv (Lưu path name myenv vào file hệ thống)
```
- Xác nhận xem env đã cài đúng chưa ?
```
conda list (hoặc)
conda env list
conda info –envs (đồng thời kiểm tra được đang dùng env nào)0
```
- Hủy bỏ mt :
```
source deactivate (Xóa path name myenv khỏi file hệ thống)
```

**- Xem danh sách các package trong env:**
```
conda list -n myenv         (Nếu env chưa kích hoạt)
conda list                  (Nếu env đã kích hoạt rồi)
conda list -n myenv scipy   (Xem thông tin package version trong env chỉ định)
```

**- Xuất ra file env để có thể share cho người khác:**
```
source activate myenv (vào môi trường đã active để có thể export được thông tin)
conda env export > environment.yml (Gửi file này cho người khác, để người ta dùng 2 để tạo env từ file này)
```
**- Xóa môi trường:**
```
conda remove --name myenv --all     (hoặc)
conda env remove --name myenv   
 
conda info --envs   (kiểm tra xem đã xóa chưa)
```








