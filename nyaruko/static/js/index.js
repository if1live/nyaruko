function enable_all_category() {
  $('.category-checkbox').each(function(i) {
    var node = this;
    node.checked = true;
  });
}

$(document).ready(function() {
  enable_all_category();

  $('#category-check-all').click(function() {
    enable_all_category();
  });
  
  $('#category-clear-all').click(function() {
    $('.category-checkbox').each(function(i) {
      this.checked = false;
    });
  });
});
