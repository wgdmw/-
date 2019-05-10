var d1 = window.location.host;
var d2 = document.domain;
//手机导航栏下拉菜单
$(function(){

	$(".menu-icon").click(function(){
		var ul=$(".menu");
		if(ul.css("display")=="none"){
			ul.slideDown();
		}else{
			ul.slideUp();
		}
	});
	
	$(".menu-icon").click(function(){
		var _name = $(this).attr("name");
		if( $("[name="+_name+"]").length > 1 ){
			$("[name="+_name+"]").removeClass("select");
			$(this).addClass("select");
		} else {
			if( $(this).hasClass("select") ){
				$(this).removeClass("select");
			} else {
				$(this).addClass("select");
			}
		}
	});
	
	$(".nav li").click(function(){
		var li=$(this).text();
		$(".menu-icon").html(li);
		$(".menu").hide();
		/*$(".menu").css({background:'#C33333'});*/
		$("div").removeClass("select") ;   
	});
});

//侧栏跟随
(function(){
   var oDiv=document.getElementById("float");
   var H=0,iE6;
   var Y=oDiv;
   while(Y){H+=Y.offsetTop;Y=Y.offsetParent};
   iE6=window.ActiveXObject&&!window.XMLHttpRequest;
   if(!iE6){
       window.onscroll=function()
       {
           var s=document.body.scrollTop||document.documentElement.scrollTop;
           if(s>H){oDiv.className="div1 div2";if(iE6){oDiv.style.top=(s-H)+"px";}}
           else{oDiv.className="div1";}    
       };
   }
})();
$('.searchBtn a').click(function(){
		$('#simplemodal-container,#searchbar').show();
	});
	$('#simplemodal-container').click(function(){
		$(this).hide();
		$('#searchbar').hide();
	});
//百度分享
document.getElementById("ckepop").innerHTML = "<div class='bdsharebuttonbox'><a href='#' class='bds_qzone' data-cmd='qzone' title='分享到QQ空间'></a><a href='#' class='bds_tsina' data-cmd='tsina' title='分享到新浪微博'></a><a href='#' class='bds_douban' data-cmd='douban' title='分享到豆瓣网'></a><a href='#' class='bds_weixin' data-cmd='weixin' title='分享到微信'></a><a href='#' class='bds_more' data-cmd='more'></a><a href='#' class='bds_count' data-cmd='count'></a></div>";
document.writeln("<scr"+"ipt>window._bd_share_config={'common':{'bdSnsKey':{},'bdText':'','bdMini':'2','bdMiniList':false,'bdPic':'','bdStyle':'0','bdSize':'24'},'share':{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</sc"+"ript>");
//百度喜欢
document.write("<script id='bdlike_shell'></script>");
var bdShare_config = {
"type":"large",
"color":"red",
"uid":"123456",
"likeText":"写的不错，赞一个！",
"likedText":"您已赞！",
"share":"yes"
};
document.getElementById("bdlike_shell").src="http://bdimg.share.baidu.com/static/js/like_shell.js?t=" + new Date().getHours();

var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?0bcaa427051a852d5f2f23fc5be80d05";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();