jQuery(function($){
	
	$('#link_sair').click(function(){
	$(this).remove()
	});
	
	if (location.href == "http://pestanalocadora.appspot.com/") {
		$('footer').addClass('footer-home');
	}else if(location.href == "http://pestanalocadora.appspot.com/servico"){
		$('footer').addClass('footer-service');
	}
	
	$('a[href="#nome"]').on('click',function(e){  
		e.preventDefault();
		$('#myModal').modal({show:true})
	});
	
   $(".tweet").tweet({
      username: "ashokramesh90",
      join_text: "auto",
      avatar_size: 0,
      count: 3,
      auto_join_text_default: "we said,",
      auto_join_text_ed: "we",
      auto_join_text_ing: "we were",
      auto_join_text_reply: "we replied to",
      auto_join_text_url: "we were checking out",
      loading_text: "loading tweets...",
      template: "{text}"
   });
}); 

/* Twitter #2 */

jQuery(function($){
   $(".ctweet").tweet({
      username: "ashokramesh90",
      join_text: "auto",
      avatar_size: 0,
      count: 1,
      auto_join_text_default: "we said,",
      auto_join_text_ed: "we",
      auto_join_text_ing: "we were",
      auto_join_text_reply: "we replied to",
      auto_join_text_url: "we were checking out",
      loading_text: "loading tweets...",
      template: "{text}"
   });
}); 

/* Support list */

$("#slist a").click(function(e){
   e.preventDefault();
   $(this).next('p').toggle(200);
});

/* Portfolio */

// filter items when filter link is clicked
$('#filters a').click(function(){
  var selector = $(this).attr('data-filter');
  $container.isotope({ filter: selector });
  return false;
});


jQuery("a[class^='prettyPhoto']").prettyPhoto({
overlay_gallery: false, social_tools: false
});