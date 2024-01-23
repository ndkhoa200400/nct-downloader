# nct-downloader

Download music from nhaccuatui.com
* Don't need to watch ads
* Download a list of tracks
* Download a playlist
* Support download with HQ (320kbps) when available
* Slugify track name if track name contains some special characters

### Prerequisites 
* Download `python`: https://www.python.org/
* Run command `pip install -r requirement.txt`

### How to use

```python
python crawl_nct.py url_1 url2
```
Tracks will be saved into folder `nhac/`, you can go there and copy to your desired directory.

For example:
```python
python crawl_nct.py https://www.nhaccuatui.com/bai-hat/anh-la-ngoai-le-cua-em-phuong-ly.0FMhI1yaOhGH.html https://www.nhaccuatui.com/bai-hat/martini-van-mai-huong.lCrctkQzaAMZ.html
```
* Result
```
Đang tải bài hát Anh Là Ngoại Lệ Của Em
+ Đã tải xong bài hát Anh Là Ngoại Lệ Của Em với chất lượng cao
Đang tải bài hát Martini
+ Đã tải xong bài hát Martini với chất lượng cao

Đã xong. Đã tải 2 bài hát
```

#### Download a playlist
You can even download a whole playlist (which is premium feature)
For example, you want to download playlist [1989 (Taylor's Version) - Taylor Swift](https://www.nhaccuatui.com/playlist/1989-taylors-version-taylor-swift.3kTTvJJwVkyc.html)
```
python crawl_nct.py https://www.nhaccuatui.com/playlist/1989-taylors-version-taylor-swift.3kTTvJJwVkyc.html
```
* Result
```
Đang tải bài hát Welcome To New York (Taylor's Version)
+ Đã tải xong bài hát Welcome To New York (Taylor's Version) với chất lượng cao
Đang tải bài hát Blank Space (Taylor's Version)
+ Đã tải xong bài hát Blank Space (Taylor's Version) với chất lượng cao
Đang tải bài hát Style (Taylor's Version)
+ Đã tải xong bài hát Style (Taylor's Version) với chất lượng cao
Đang tải bài hát Out Of The Woods (Taylor's Version)
+ Đã tải xong bài hát Out Of The Woods (Taylor's Version) với chất lượng cao
Đang tải bài hát All You Had To Do Was Stay (Taylor's Version)
+ Đã tải xong bài hát All You Had To Do Was Stay (Taylor's Version) với chất lượng cao
Đang tải bài hát Shake It Off (Taylor's Version)
+ Đã tải xong bài hát Shake It Off (Taylor's Version) với chất lượng cao
Đang tải bài hát I Wish You Would (Taylor's Version)
+ Đã tải xong bài hát I Wish You Would (Taylor's Version) với chất lượng cao
Đang tải bài hát Bad Blood (Taylor's Version)
+ Đã tải xong bài hát Bad Blood (Taylor's Version) với chất lượng cao
Đang tải bài hát Wildest Dreams (Taylor's Version)
+ Đã tải xong bài hát Wildest Dreams (Taylor's Version) với chất lượng cao
Đang tải bài hát How You Get The Girl (Taylor's Version)
+ Đã tải xong bài hát How You Get The Girl (Taylor's Version) với chất lượng cao
Đang tải bài hát This Love (Taylor’s Version)
+ Đã tải xong bài hát This Love (Taylor’s Version) với chất lượng cao
Đang tải bài hát I Know Places (Taylor's Version)
+ Đã tải xong bài hát I Know Places (Taylor's Version) với chất lượng cao
Đang tải bài hát Clean (Taylor's Version)
+ Đã tải xong bài hát Clean (Taylor's Version) với chất lượng cao
Đang tải bài hát Wonderland (Taylor's Version)
+ Đã tải xong bài hát Wonderland (Taylor's Version) với chất lượng cao
Đang tải bài hát You Are In Love (Taylor's Version)
+ Đã tải xong bài hát You Are In Love (Taylor's Version) với chất lượng cao
Đang tải bài hát New Romantics (Taylor's Version)
+ Đã tải xong bài hát New Romantics (Taylor's Version) với chất lượng cao
Đang tải bài hát "Slut!" (Taylor's Version) (From The Vault)
> Đổi tên bài hát "Slut!" (Taylor's Version) (From The Vault) => slut-taylor-s-version-from-the-vault
+ Đã tải xong bài hát slut-taylor-s-version-from-the-vault với chất lượng cao
Đang tải bài hát Say Don't Go (Taylor's Version) (From The Vault)
+ Đã tải xong bài hát Say Don't Go (Taylor's Version) (From The Vault) với chất lượng cao
Đang tải bài hát Now That We Don't Talk (Taylor's Version) (From The Vault)
+ Đã tải xong bài hát Now That We Don't Talk (Taylor's Version) (From The Vault) với chất lượng cao
Đang tải bài hát Suburban Legends (Taylor's Version) (From The Vault)
+ Đã tải xong bài hát Suburban Legends (Taylor's Version) (From The Vault) với chất lượng cao
Đang tải bài hát Is It Over Now? (Taylor's Version) (From The Vault)
> Đổi tên bài hát Is It Over Now? (Taylor's Version) (From The Vault) => is-it-over-now-taylor-s-version-from-the-vault
+ Đã tải xong bài hát is-it-over-now-taylor-s-version-from-the-vault với chất lượng cao

Đã xong. Đã tải 21 bài hát
```
