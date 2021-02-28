function copyText (text) {

    const element = document.createElement('textarea');
    element.value = text;
    element.setAttribute('readonly', '');
    element.style.position = 'absolute';
    element.style.left = '-9999px';
    document.body.appendChild(element);

    const selected =
    document.getSelection().rangeCount > 0
      ? document.getSelection().getRangeAt(0)
      : false;
  
  
    element.select();
    try{
      document.execCommand('copy');
      alert('Copied Magnet Link to clipboard.');
    }
    catch(err){
      alert("Error Copying Magnet Link to clipboard use link button to access magnet link");
    }
    document.body.removeChild(element);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
  
  }