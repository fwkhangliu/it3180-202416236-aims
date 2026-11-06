# Bằng chứng thực hành Lab 01

MSSV **202416236** - GitHub **fwkhangliu**. Các giá trị bên dưới lấy từ lệnh đã chạy và API GitHub trong buổi thực hành ngày 2026-11-06 (Asia/Saigon).

## Môi trường và xác thực

- Python 3.13.13; Git 2.56.0.windows.4; GitHub CLI 2.103.3.
- Git/GitHub CLI portable được tải từ repository chính thức, kiểm tra SHA256 của asset trước khi giải nén.
- Git global: Khang / khanghoang242@gmail.com; defaultBranch master; autocrlf true; code --wait; pull.rebase false.
- Đã tạo ED25519 riêng, thêm public key lên đúng tài khoản, nạp ssh-agent/ssh-add.
- SSH trả lời: `Hi fwkhangliu! You've successfully authenticated, but GitHub does not provide shell access.` Exit 1 là hành vi bình thường vì GitHub không cung cấp shell.
- Repo public khởi tạo rỗng, remote `git@github.com:fwkhangliu/it3180-202416236-aims.git`, default branch master.

## Commit và hoàn tác thật

| Bước | SHA / kết quả |
| --- | --- |
| Initial commit, chỉ README + .gitignore + .gitattributes | `fb205e7417c23407ff2bcc1c065922559f6773ce` |
| Thêm 3 file Python ở gốc trong commit riêng | `471fcbebb684b0554e90b3b69c0653a6b3aefe6d` |
| Message sai, CHƯA PUSH | `e9af9001446d00d4ad62381f715095687700d897` |
| Commit sau amend, mới được push | `1dd951d40e1e98c1fca885d94949f1c2d9f58016` |
| origin/master khi amend | `471fcbebb684b0554e90b3b69c0653a6b3aefe6d` |
| git restore cart.py | Comment nháp biến mất; status sạch |
| git restore --staged main.py | `M ` chuyển thành ` M`; diff --staged rỗng, working diff vẫn còn |

Nhật ký thực tế các lệnh phần C được trích tại [lab01-undo-operations.jsonl](evidence/lab01-undo-operations.jsonl). Nhật ký toàn bộ nằm ngoài repository ở workspace `lab-evidence/lab01/commands.jsonl`; không chứa nội dung private key hoặc token. Reflog trên máy còn cả SHA trước/sau amend; không giả định reflog được push lên GitHub.

## Refactor qua Pull Request

- [https://github.com/fwkhangliu/it3180-202416236-aims/pull/1](https://github.com/fwkhangliu/it3180-202416236-aims/pull/1) đã **MERGED** vào master lúc `2026-11-06T14:36:37Z`.
- Commit di chuyển: `ed9749a785831b3ecc5e2dac02bf311c76f635d2`.
- Commit sửa import: `30a0b8111ceed0994c652d990310cb542bceed61`.
- Merge commit: `95136d2c1ae29fe8c8435d2e714e935161499b52`.
- GitHub Files changed ghi `renamed` cho `cart.py -> aims/cart.py`, `dvd.py -> aims/dvd.py`; cả hai có `changes: 0`.
- Blob cart trước/sau: `fe045c3cfc36c631a3e6174663a76f74f543c6d0`.
- Blob dvd trước/sau: `0f5b2e3533aa7a0fd53600f0c39db1a00d19e050`.
- Nhánh refactor đã được xóa ở remote và local; đã pull và fetch --prune.

## Kiểm tra chương trình và phạm vi

Trước và sau refactor, `python main.py` đều exit 0, in ba lần `The disc has been added` rồi `Total cost: 63.89 $`.

`git check-ignore -v` xác nhận cache, .venv và .vscode bị ignore. `git ls-files` không có __pycache__. Nội dung Cart/DVD không đổi. Chưa có print_cart/search/test/version/CHANGELOG/CI, đúng trạng thái Lab 01; lỗi giới hạn vẫn để dành Lab 03.

## Bước đóng baseline

PR tài liệu này cần merge trước khi tạo `release/lab01` để baseline chứa cả câu trả lời. Sau đó chạy lại main, xem graph/remote và kiểm tra `git rev-parse origin/master origin/release/lab01` bằng nhau. Báo cáo checkpoint cuối cùng với SHA baseline thực tế được lưu ngoài repo trong workspace để tránh một commit báo cáo lại làm thay đổi chính baseline đang báo cáo. Chưa gắn tag; các tag baseline cũ được tạo ở Lab 04.
