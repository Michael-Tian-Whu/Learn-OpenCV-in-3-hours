<!--
 * @Author: WHURS-THC
 * @Date: 2022-10-22 15:45:03
 * @LastEditTime: 2022-10-25 16:29:00
 * @Description: 
-->
# Note By THC

## 1. 分辨率

- $VGA = 640 *480$  
$HD = 1280* 120$  
$FHD = 1920 *1080$  
$4K = 3840* 2160$  
$2^8=256=8bit=1byte$

## 2. waitkey

```python
cv2.waitKey(1) & 0xFF == ord('q'):
```

>cv2.waitKey(delay)返回值：  

1. 等待期间有按键：返回按键的ASCII码（比如：q的ASCII码为113）
2. 等待期间没有按键：返回 -1  

>ord(‘q’)：返回q的ASCII值
 
> 0xFF=1111 1111   `&|^即与或异或`  取<255的部分。

在所有系统中，可以通过读取返回值的最后一个字节来保证只读取ASCII码，即与0xFF做与运算，即可保证获得ASCII码  
为何做掩码运算是因为已经发现在Linux中的某些情况下（when OpenCV uses GTK as its backend GUI），waitKey()可能返回超过ASCII的keycode，所以这是为了防止在某些情况下产生bug。  

https://blog.csdn.net/Dandelion_2/article/details/108225453

## 3.BGR

Python-Opencv中彩色图像以`BGR`形式储存

## 4.cv2.bitwise_and

```python
cv2.bitwise_and(img1,img2,mask=mask)
```

**与运算**：在`mask`掩膜的范围内，对两个图像进行二进制与运算  

1. 若`img1=img2`则输出图像掩膜范围内的部分。
2. 若`img1!=img2`则输出二者每个像素点中较小的那个点，并组成新的图像。  
