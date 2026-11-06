# Thảo luận Lab 03

MSSV: 202416236 - GitHub: fwkhangliu

## Merge base là gì?

Là tổ tiên chung tốt nhất của hai commit, dùng làm mốc so sánh trong three-way merge. Hai nhánh thông điệp được tạo từ cùng baseline và sửa cùng dòng nên đã phát sinh conflict thật.

## Vì sao master/release phải dùng revert?

Revert tạo commit đảo ngược và giữ nguyên SHA/lịch sử người khác đã dùng. Reset/rebase viết lại lịch sử nên chỉ thực hành trên topic/undo-practice và topic/conflict-rebase-practice chưa push. Đã dùng reset soft/mixed/hard, reflog và tạo topic/recovered-undo để khôi phục commit.

## Truy vết

Issue giới hạn giỏ được đóng bởi PR có Fixes, commit test FAIL đứng trước fix PASS. Bugfix discount có base feature/discount; cuối Lab có 4 tests OK.
