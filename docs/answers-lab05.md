# Thảo luận Lab 05

MSSV: 202416236 - GitHub: fwkhangliu

## Upstream first và release first

Upstream first sửa trên master trước rồi backport, giảm nguy cơ quên bản sửa ở dòng phát triển nhưng có thể cần điều chỉnh nhiều cho bản cũ. Release first sửa đúng cấu hình đang gây lỗi và phát hành bản vá nhanh; phải chủ động lan truyền sang master và các release bị ảnh hưởng. Bài này dùng release first.

## Vì sao không merge toàn bộ hotfix vào master?

Commit bump 1.0.1 chỉ dành cho dòng 1.0.x, trong khi master đã là 1.1.0. Tách test+fix và bump thành hai commit, rồi chỉ cherry-pick -x commit fix. Footer lưu SHA nguồn để kiểm toán.

## Vì sao chưa gắn v1.1.0 ở phần A?

Release/lab05 còn phải nhận hotfix. Tag phát hành đã chia sẻ phải bất biến; nếu đã phát hành v1.1.0 trước đó thì bản vá tiếp theo phải là v1.1.1.

## Lệnh nào phát hiện quên release/lab05?

Vòng kiểm tra hành vi v1.0.1/v1.1.0/master sẽ trả 0 cho dòng thiếu fix. Log grep footer SHA nguồn cũng sẽ thiếu một trong hai bản cherry-pick; git cherry -v master release/lab05 giúp kiểm tra patch tương đương. git tag --contains chỉ xét tổ tiên commit, không coi hai cherry-pick là cùng SHA.
