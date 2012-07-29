function enable_all_category() {
  $('.category-checkbox').each(function(i) {
    var node = this;
    node.checked = true;
  });
}

function validate_search_form() {
  var keyword = document.forms["search_form"]["keyword"].value
  keyword = $.trim(keyword);
  if(keyword == '') {
    return false;
  }
  return true;
}

$(document).ready(function() {
  $('#category-check-all').click(function() {
    enable_all_category();
  });
  
  $('#category-clear-all').click(function() {
    $('.category-checkbox').each(function(i) {
      this.checked = false;
    });
  });
});
