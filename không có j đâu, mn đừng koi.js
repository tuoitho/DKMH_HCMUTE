const fetch = require('node-fetch');
const cheerio = require('cheerio');
// const lp='WEPR330479_02'
const lp='1241WEPR330479_02'
stt=1


// kiểm tra danh sách lớp, nếu b chạy cũng đồng nghĩa đang ddos trang e-bills, k tin thì chạy sau đó truy cập trang e-bills đy
const getName=(id) =>
    fetch("https://e-bills.vn/pay/hcmute?customer="+id, {
        "headers": {
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
          "cache-control": "max-age=0",
          "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"Windows\"",
          "sec-fetch-dest": "document",
          "sec-fetch-mode": "navigate",
          "sec-fetch-site": "none",
          "sec-fetch-user": "?1",
          "upgrade-insecure-requests": "1"
        },
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": null,
        "method": "GET",
        "mode": "cors",
        "credentials": "include"
      }).then(function (response) {
        // console.log(response)
        const resp= response.text();
        return resp
        
      }).then(function (data) {
        const $ = cheerio.load(data);
        if (!data.includes(lp)) return;
        const name = $('#hoten').val();
        console.log(stt++,id,name)
        
      })
      .catch(function (err){
        console.log(err);
        // dung vong lap
      });
    

getName(22110442)
for (let i = 22110285; i < 22110462; i++) {
    getName(i)
}
// for (let i = 22133001; i < 22133067; i++) {
//     getName(i)
// }
// for (let i = 22162001; i<= 22162057; i++) {
//     getName(i)
// }
