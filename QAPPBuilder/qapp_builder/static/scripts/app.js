// NOTE: This is critical! Bootstrap Flatly attaches fade to the popover element, so it must be removed manually.
//       If not removed, the fade class renders popover elements invisible.
function delayRemoveFade() {
  setTimeout($('.fade').removeClass('fade'), 300);
}

setTimeout(function () {
  $("#save_success").addClass('fade');
}, 2000);

function fromEditToDetail() {
  var path = window.location.pathname.replace('edit', 'detail');
  window.location.href = path;
}

function rowClick(id) {
  // const activeClass = 'table-row-active';
  const activeClass = 'usa-alert usa-alert--success';
  console.log('rowclick', id);
  $("tr").removeClass(activeClass);
  $("#" + id).addClass(activeClass);
  $("i").removeAttr('aria-disabled');
  $("i").attr('id', id);
}
