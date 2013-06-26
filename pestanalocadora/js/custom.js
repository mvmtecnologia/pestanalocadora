jQuery(function($){
	
	$('.msg').popover({trigger:'hover'});
	
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
});