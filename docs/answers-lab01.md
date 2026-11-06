# Trả lời thảo luận Lab 01

MSSV: **202416236**. GitHub: **fwkhangliu**. Nguồn câu hỏi: trang 19 và 26 của tài liệu thực hành IT3180.

## 1. Cấu hình --global lưu ở đâu, khác --local thế nào? (trang 19)

Trong môi trường Windows này, `git config --global` ghi vào `C:/Users/Admin/.gitconfig` (tức `~/.gitconfig`). `git config --list --show-origin` hoặc `git config --show-origin --get user.email` cho biết nguồn của giá trị thực tế; Git cũng hỗ trợ vị trí cấu hình toàn cục theo XDG khi được thiết lập.

`--global` áp dụng cho các repository của tài khoản hệ điều hành hiện tại. `--local` áp dụng riêng repository, thường lưu trong `.git/config`, và được ưu tiên hơn giá trị global cùng khóa. Ví dụ, `user.name` và `user.email` ở global định danh tác giả commit; `core.sshCommand` ở local của repo này chọn đúng khóa/kết nối SSH dành cho bài thực hành.

Các giá trị đã cấu hình trong bài: nhánh mặc định `master`, `core.autocrlf=true` cho Windows, editor `code --wait`, `pull.rebase=false`, tên `Khang` và email do sinh viên cung cấp. Thông tin tài khoản GitHub dùng để xác thực độc lập với tên/email tác giả commit.

## 2. Vì sao dùng git mv? (trang 26)

`git mv cart.py aims/cart.py` di chuyển file trong working directory và cập nhật index ngay, tránh quên stage việc bỏ đường dẫn cũ hoặc thêm đường dẫn mới. Có thể đạt kết quả tương đương bằng thao tác di chuyển thông thường rồi `git add` các đường dẫn liên quan.

Git lưu snapshot; `git mv` không tạo một bản ghi rename đặc biệt bảo đảm giữ lịch sử. Khi xem diff/log, Git suy luận rename bằng độ tương đồng nội dung. Bài này tách commit di chuyển khỏi commit sửa import, nên `cart.py` và `dvd.py` được nhận diện rename 100%. `git log --oneline --follow -- aims/cart.py` truy được commit thêm mã nguồn ban đầu.

Trong PR refactor, hai file được GitHub hiển thị `RENAMED`, không phải một cặp xóa/thêm độc lập. Blob của mỗi file trước và sau di chuyển giống hệt nhau.

## 3. release/lab01 có phải baseline không? (trang 26)

Có. Khi đã kiểm tra chương trình, merge các PR cần nộp và tạo `release/lab01` từ `master`, commit được nhánh đó trỏ tới xác định cấu hình đã thống nhất để nộp Lab 01. Tại checkpoint này, `origin/master` và `origin/release/lab01` phải có cùng SHA.

Nhánh là con trỏ có thể di chuyển, nên một nhánh release không tự tạo ra tính bất biến. Các thay đổi sau khi nộp phải tuân thủ quy trình bảo trì qua nhánh/PR thích hợp, không commit trực tiếp. Ở Lab 04, annotated tag `v0.1.0` sẽ định danh chính xác baseline Lab 01; tag đã chia sẻ không được xóa hay di chuyển. Khi Lab 02 phát triển tiếp trên `master`, không yêu cầu hai nhánh này tiếp tục bằng nhau.

## 4. Vì sao không commit thẳng master dù làm một mình? (trang 26)

Nhánh công việc giữ thay đổi đang thực hiện tách khỏi cấu hình tích hợp. PR ghi rõ mục đích, diff, cách kiểm thử và kết quả merge; các liên kết này giúp kiểm toán, thảo luận và hoàn tác về sau. Làm một mình vẫn có ích khi tự đọc diff trước khi tích hợp và có cùng quy trình nếu sau này thêm cộng tác viên.

PDF cho phép làm một mình với `Require approvals=0`, nhưng vẫn yêu cầu PR (trang 13/29). Điều này không đồng nghĩa với đã có reviewer hay approval của người khác. Lab 01 có ngoại lệ khởi tạo và bài tập amend ở phần A-C trên master; từ phần refactor trở đi, thay đổi trong bài này đi qua nhánh và PR.

## 5. Ba vùng làm việc và thực hành hoàn tác

Working directory là nội dung file đang chỉnh; staging area (index) là snapshot chuẩn bị commit; local repository lưu các commit. `push` cập nhật repository trên GitHub.

| Lệnh đã thực hành | Tác dụng đã quan sát |
| --- | --- |
| `git restore cart.py` | Bỏ đúng đoạn comment nháp chưa stage, trả nội dung file về index; `git status --short` trở lại rỗng. |
| `git restore --staged main.py` | Bỏ thay đổi nháp khỏi index, giữ nguyên nội dung sửa trong working directory; trạng thái đổi từ `M ` sang ` M`. |
| `git commit --amend -m "docs: add Python requirement to README"` | Thay commit message sai trên commit chưa push; SHA thay đổi, reflog giữ bản ghi trước/sau. |

Không dùng amend/reset/rebase để viết lại lịch sử đã chia sẻ. Với thay đổi đã chia sẻ cần hoàn tác, sẽ thực hành `revert` qua nhánh/PR ở Lab 03.
