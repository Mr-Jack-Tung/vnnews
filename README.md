# vnnews crawler
A Python package that helps crawl updates from top Vietnamese news providers.

---
<div id="badges" align="center">
<img src="https://img.shields.io/pypi/pyversions/vnnews?logoColor=brown&style=plastic" alt= "Version"/>
<img src="https://img.shields.io/pypi/dm/vnnews" alt="Download Badge"/>
<img src="https://img.shields.io/github/last-commit/thinh-vu/vnnews" alt="Commit Badge"/>
<img src="https://img.shields.io/github/license/thinh-vu/vnnews?color=red" alt="License Badge"/>
</div>

# II. REFERENCES
## 2.1. How to use this package?
- You can install the latest `vnnews` crawler version from source with the following command:
`pip install git+https://github.com/thinh-vu/vnnews.git@main`

_(*) You might need to insert a `!` before your command when running terminal commands on Google Colab._

- To start using functions, you need to import them: `from vnnews import *`

## 2.2. List of Popular Online news for investors
1. [VN Express](https://vnexpress.net/)
2. [Tuổi trẻ Online](https://tuoitre.vn/)
3. [CafeF](https://cafef.vn/)
4. [Cafebiz](https://cafebiz.vn/)
5. [Kinh tế Sài Gòn Online](https://thesaigontimes.vn/)
6. [VN Economy](https://vneconomy.vn/)
7. [Pháp Luật Tp.HCM](https://plo.vn/)
8. [Đầu tư Online](https://baodautu.vn/)
9. [Nhịp cầu đầu tư](https://nhipcaudautu.vn/)
10. [Diễn đàn doanh nghiệp](https://diendandoanhnghiep.vn/)
11. [Diễn đàn kinh tế Việt Nam - Vietnamnet](https://vef.vn/)
12. [Forbes Việt Nam](https://forbes.vn/)
13. [Vietstock](https://vietstock.vn/)
14. [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/)
15. [Cafe Land](https://cafeland.vn/)
16. [Kenh14](https://kenh14.vn/)
17. [Dân trí](https://dantri.com.vn/)
18. [Thanh niên](https://thanhnien.vn/)
19. [Vietnamnet](http://vietnamnet.vn/)
20. [Nhân dân điện tử](http://www.nhandan.com.vn/)
21. [Lao động](http://laodong.com.vn/)
22. [Đời sống & pháp luật](http://www.doisongphapluat.com/)

## 2.3. Function references

- `url_extract (url, key, tag_class='', type='link', bs_on=True, user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:11.0) Gecko/20100101')`
    - Purpose: Extract article info from a news source using BeautifulSoup to pull data from HTML/XML web page.
    - Arguments:
      - url (:obj:`str`, required): url of the target news source. Eg. 'https://cafef.vn/'
      - key (:obj:`str`, required): HTML tag which contains the information that you want to extract. Eg. 'h3', 'article', 'div'
      - tag_class (:obj:`str`, required): The HTML class attribute specifies one or more class names for an element. Eg. 'pdate' in the tag <span class="pdate">19-11-2022 - 15:32 PM </span> on CafeF.
      - type (:obj:`str`, optional): 'link' as default to extract only the article link from a news homepage. Use blank value `''` when extracting article detail on the article page.
      - bs_on (:obj:`str`, optional): `True` as default. Input blank `''` when the issue is raised.
      - user_agent (:obj:`str`, optional): The default value for Desktop has been provided. You can find more user agent value here: https://developers.whatismybrowser.com/useragents/explore/operating_system_name/

- `fix_url(host, url)`
  - Purpose: Extract article info from a news source using BeautifulSoup to pull data from HTML/XML web page.
  - Arguments:
    - host (:obj:`str`, required): the host name of the news source. Eg. 'https://vneconomy.vn
    - url (:obj:`str`, required): the url string of the target news source. This might not contain the host at the beginning. Eg. '/de-viet-nam-thanh-digital-hub-cua-khu-vuc-vao-nam-2030-e290.htm'

## 2.4. Let's get our hands dirty
1. [VN Express](https://vnexpress.net/)
   - Get the list of article urls: `url_extract('https://vnexpress.net/kinh-doanh', key='h3')`
   - Extract article details: `url_extract('https://vnexpress.net/thuong-mai-va-dau-tu-ben-vung-se-giup-apec-ung-pho-nguy-co-suy-thoai-4538015.html', key='span', tag_class='date', type='')`
2. [Tuổi trẻ Online](https://tuoitre.vn/)
   - Get the list of article urls: `url_extract('https://tuoitre.vn/phap-luat.htm', key='h3')`
   - Extract article details: `url_extract('https://tuoitre.vn/gap-thu-tuong-xuc-dong-chuyen-co-giao-mam-non-miet-mai-lam-thien-nguyen-cho-vung-xa-20221119175021292.htm', key='div', tag_class='date-time', type='')`
3. [CafeF](https://cafef.vn/)
   - Get the list of article urls:  `url_extract('https://cafef.vn/bat-dong-san.chn', key='h3', type='link')`
   - Extract article details: `url_extract('https://cafef.vn/dau-se-la-phan-khuc-bds-giu-duoc-nhiet-trong-thoi-gian-toi-2022111913083069.chn', key='span', tag_class='pdate', type='')`
4. [Cafebiz](https://cafebiz.vn/)
   - Get the list of article urls:  `url_extract('https://cafebiz.vn/vi-mo.chn', key='h3', type='link', bs_on='')`
   - Extract article details: `url_extract('https://cafebiz.vn/tai-sao-nha-o-my-la-tai-san-con-o-nhat-ban-thi-lai-chang-khac-gi-hang-tieu-dung-176221119095831295.chn', key='span', tag_class='time', type='')`
5. [Kinh tế Sài Gòn Online](https://thesaigontimes.vn/)
   - Get the list of article urls:  `url_extract('https://thesaigontimes.vn/', key='h3', type='link', bs_on='')`
   - Extract article details: `url_extract('https://thesaigontimes.vn/kinh-te-tuan-hoan-mo-ra-nhung-mo-hinh-kinh-doanh-moi/', key='time', tag_class='', type='')`
6. [VN Economy](https://vneconomy.vn/)
   - Get the list of article urls:  `url_extract('https://vneconomy.vn/', key='h3', type='link', bs_on=False)`
   - Extract article details: `url_extract('https://vneconomy.vn/xuat-khau-det-may-van-tu-tin-voi-muc-tieu-42-ty-usd.htm', key='div', tag_class='detail__meta', type='')`
7. [Pháp Luật Tp.HCM](https://plo.vn/)
   - Get the list of article urls:  `url_extract('https://m.plo.vn/phap-luat/', key='h3', type='link')[0][1]`
   - Extract article details: `test = url_extract('https://plo.vn/dieu-tra-trung-tam-dang-kiem-cap-so-song-sinh-cho-xe-tai-post705918.html', key='time', tag_class='', type='')`
8. [Đầu tư Online](https://baodautu.vn/)
   - Get the list of article urls:  `url_extract('https://baodautu.vn/', key='article', type='link', bs_on='')`
   - Extract article details: `url_extract('https://baodautu.vn/nguoi-dan-rong-ra-cau-cuu-khi-nao-co-so-do-tu-du-an-cua-cong-ty-bach-dat-an-d177946.html', key='span', tag_class='post-time', type='')`
9.  [Nhịp cầu đầu tư](https://nhipcaudautu.vn/)
   - Get the list of article urls:  `url_extract('https://m.nhipcaudautu.vn/kinh-doanh/', key='article', type='link', bs_on='', user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X)')`
   - Extract article details: `url_extract('https://m.nhipcaudautu.vn/ti-le-don-bay-tai-chinh-toan-thi-truong-giam-dan-tu-quy-i-3348999/', key='span', tag_class='date-post', type='')`
10.  [Diễn đàn doanh nghiệp](https://diendandoanhnghiep.vn/)
     - Get the list of article urls:  `url_extract('https://diendandoanhnghiep.vn/', key='h3', type='link', bs_on='')`
     - Extract article details: `url_extract('https://diendandoanhnghiep.vn/https-diendandoanhnghiep-vn-dien-mat-troi-mai-nha-can-hoan-thien-co-che-ho-tro-doanh-nghiep-phat-trien-225626-html-e313.html', key='span', tag_class='created_time', type='')`
11.  [Diễn đàn kinh tế Việt Nam - Vietnamnet](https://vef.vn/)
     - Get the list of article urls:  `url_extract('https://vef.vn/diem-nong/', key='article', type='link', bs_on='')`
     - Extract article details: ``
12. [Forbes Việt Nam](https://forbes.vn/)
    - Get the list of article urls:  `url_extract('https://forbes.vn', key='h3', type='link', bs_on='')`
    - Extract article details: `url_extract('https://forbes.vn/m-village-cua-nguyen-hai-ninh-xay-lang-trong-pho/', key='div', tag_class='forbes-single__heading-time', type='')`
13.  [Vietstock](https://vietstock.vn/)
     - Get the list of article urls:  `url_extract('https://vietstock.vn/', key='h4', type='link', bs_on='')`
     - Extract article details: `url_extract('https://vietstock.vn/2022/11/thieu-hut-iphone-14-nguoi-dung-viet-lua-chon-iphone-doi-cu-4264-1017483.htm', key='span', tag_class='date', type='')`
14. [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/)
    - Get the list of article urls: Doesn't work `url_extract('https://m.tinnhanhchungkhoan.vn/', key='h2', type='link', bs_on='')`
    - Extract article details: `url_extract('https://www.tinnhanhchungkhoan.vn/big-trends-sau-con-mua-troi-lai-sang-post310328.html', key='time', tag_class='', type='')`
15. [Cafe Land](https://cafeland.vn/)
    - Get the list of article urls:  `url_extract('https://cafeland.vn/', key='h3', type='link', bs_on='')`
    - Extract article details: `url_extract('https://cafeland.vn/phan-tich/bien-doi-khi-hau-dang-leo-thang-nhung-doanh-nghiep-chu-yeu-doi-pho-114941.html', key='div', tag_class='info-date right', type='')`
16. [Kenh14](https://kenh14.vn/)
    - Get the list of article urls:  `url_extract('https://m.kenh14.vn/doi-song.chn', key='h3', type='link')`
    - Extract article details: `url_extract('https://m.kenh14.vn/phia-sau-nhung-gen-z-okela-co-luc-that-bai-co-luc-khong-on-lam-nhung-chua-bao-gio-ngung-no-luc-20221119153833146.chn', key='span', tag_class='kbwcm-time', type='')`
17. [Dân trí](https://dantri.com.vn/)
    - Get the list of article urls:  `url_extract('https://dantri.com.vn/', key='h3', type='link', bs_on='')`
    - Extract article details: `url_extract('https://dantri.com.vn/the-gioi/moscow-cao-buoc-ukraine-kich-dong-xung-dot-quan-su-nga-nato-20221119145209276.htm', key='time', tag_class='author-time', type='')`
18. [Thanh niên](https://thanhnien.vn/)
    - Get the list of article urls:  ``
    - Extract article details: ``
19. [Vietnamnet](http://vietnamnet.vn/)
    - Get the list of article urls:  ``
    - Extract article details: ``
20. [Nhân dân điện tử](http://www.nhandan.com.vn/)
    - Get the list of article urls:  ``
    - Extract article details: ``
21. [Lao động](http://laodong.com.vn/)
    - Get the list of article urls:  ``
    - Extract article details: ``
22. [Đời sống & pháp luật](http://www.doisongphapluat.com/)
    - Get the list of article urls:  ``
    - Extract article details: ``

# III. APENDICES
- [Demo video](https://youtu.be/S_Jx_TgSTTw): How to select the key 
- Explore User Agents by Operating System: [here](https://developers.whatismybrowser.com/useragents/explore/operating_system_name/)

# IV. 🙋‍♂️ CONTACT INFORMATION
You can contact me at one of my social network profiles:

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/thinh-vu">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.messenger.com/t/mr.thinh.ueh">
    <img src="https://img.shields.io/badge/Messenger-00B2FF?style=for-the-badge&logo=messenger&logoColor=white" alt="Messenger Badge"/>
  <a href="https://www.youtube.com/channel/UCYgG-bmk92OhYsP20TS0MbQ">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  </a>
    <a href="https://github.com/thinh-vu">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github Badge"/>
  </a>
</div>

---

If you want to support my open-source projects, you can "buy me a coffee" via [Patreon](https://patreon.com/thinhvu?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator) or Momo e-wallet (VN). Your support will help to maintain my blog hosting fee & to develop high-quality content.

![momo-qr](https://github.com/thinh-vu/vnstock/blob/main/src/momo-qr-thinhvu.jpeg?raw=true)