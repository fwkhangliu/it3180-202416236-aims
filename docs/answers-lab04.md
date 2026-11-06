# Thảo luận Lab 04

MSSV: 202416236 - GitHub: fwkhangliu

## Vì sao chuẩn bị trên master trước release?

Chuẩn bị trên topic/prepare-release-1.0.0 rồi PR vào master để mã, version và changelog đã được kiểm tra thống nhất trước khi tạo baseline. Không chỉnh trực tiếp master hay release.

## Vì sao release không merge ngược master?

Release là dòng bảo trì cấu hình cũ. Merge cả dòng có thể kéo metadata phiên bản cũ và thay đổi không phù hợp vào phát triển hiện tại. Chỉ đưa commit sửa lỗi cần thiết bằng cherry-pick -x.

## So sánh GitFlow

GitFlow có main và develop, release thường được tích hợp vào cả hai. Release Flow học phần có master và các release/labXX độc lập, dùng PR và cherry-pick cho bảo trì.

## Vì sao 1.0.0 thay vì 0.4.0?

0.x thể hiện giai đoạn chưa ổn định. 1.0.0 là baseline ổn định đầu tiên với API/chức năng được thống nhất; không phải cứ qua thêm một Lab là bắt buộc tăng MINOR.
