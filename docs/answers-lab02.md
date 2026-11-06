# Thảo luận Lab 02

MSSV: 202416236 - GitHub: fwkhangliu

## Vì sao đồng bộ master trước PR?

Để phát hiện xung đột sớm và kiểm tra tính năng cùng mã mới đã tích hợp. Dev 2 đã fetch và merge origin/master trước PR tìm kiếm.

## Khi nào không được rebase?

Không viết lại commit đã được chia sẻ hoặc nhánh master/release. Rebase chỉ dùng trên lịch sử riêng chưa chia sẻ; Rebase and merge do GitHub tạo commit mới khi tích hợp PR là thao tác được đề yêu cầu.

## feature và topic khác nhau thế nào?

feature dành cho chức năng người dùng như in/tìm giỏ hàng; topic dành cho tài liệu/cấu hình như PR template và use case. Cả hai đi qua PR.

## Giới hạn nghiệm thu

Solo approvals=0 theo PDF. Chưa có reviewer thật nên mục Changes requested → Approved chưa đạt; không tạo approval giả.
