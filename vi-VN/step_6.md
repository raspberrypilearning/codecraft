## Tạo tài nguyên gỗ mới

Hãy tạo ra một nguồn tài nguyên gỗ mới. Để làm điều này, bạn sẽ cần phải thêm vào một số biến trong bạn `variables.py` tập tin.

+ Đầu tiên, bạn cần cung cấp cho tài nguyên mới của bạn một số. Sau đó, bạn sẽ có thể sử dụng từ `GOOD` trong mã của mình thay vì số 4.
    
    ![ảnh chụp màn hình](images/craft-wood-const.png)

+ Bạn nên thêm tài nguyên `GOOD` vào danh sách `tài nguyên`.
    
    ![ảnh chụp màn hình](images/craft-wood-resources.png)

+ Bạn cũng nên đặt tên cho tài nguyên của mình, tên này sẽ được hiển thị trong kho.
    
    ![ảnh chụp màn hình](images/craft-wood-name.png)
    
    Lưu ý dấu phẩy `,` ở cuối dòng trên.

+ Tài nguyên của bạn cũng sẽ cần một hình ảnh. Dự án đã bao gồm một hình ảnh gọi là `wood.gif`, bạn nên thêm vào từ điển `kết cấu`.
    
    ![ảnh chụp màn hình](images/craft-wood-texture.png)

+ Thêm số lượng tài nguyên của bạn sẽ có trong `kho` của bạn để bắt đầu.
    
    ![ảnh chụp màn hình](images/craft-wood-inventory.png)

+ Cuối cùng, thêm chìa khóa mà bạn sẽ nhấn để đặt gỗ trên thế giới.
    
    ![ảnh chụp màn hình](images/craft-wood-placekey.png)

+ Chạy dự án của bạn để kiểm tra nó. Bạn sẽ thấy rằng bây giờ bạn có tài nguyên 'gỗ' mới trong kho của mình.
    
    ![ảnh chụp màn hình](images/craft-wood-test.png)

+ Không có gỗ trong thế giới của bạn! Để khắc phục điều này, hãy nhấp vào tệp `main.txt` của bạn và tìm hàm có tên là `createdRandomWorld ()`.
    
    ![ảnh chụp màn hình](images/craft-wood-random1.png)
    
    Mã này tạo một số ngẫu nhiên trong khoảng từ 0 đến 10 và sử dụng số đó để quyết định tài nguyên nào sẽ được đặt:
    
    + 1 hoặc 2 = nước
    + 3 hoặc 4 = cỏ
    + bất cứ điều gì khác = DIRT

+ Thêm mã này để thêm gỗ vào thế giới của bạn bất cứ khi nào `ngẫu nhiên` là 5.
    
    ![ảnh chụp màn hình](images/craft-wood-random2.png)

+ Kiểm tra dự án của bạn một lần nữa. Lần này, bạn sẽ thấy một số gỗ xuất hiện trong thế giới của bạn.
    
    ![ảnh chụp màn hình](images/craft-wood-test2.png)