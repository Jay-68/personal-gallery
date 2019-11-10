function copy(element) {
  $(element).select();
  document.execCommand("copy");
}