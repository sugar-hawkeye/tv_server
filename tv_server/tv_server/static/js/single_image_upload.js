/**
 * Created by wim on 17/3/30.
 */

function readFileInfo(source){
    var file = document.getElementById(source).files[0];
    if(file){
        var size = 0;
        if(file.size > 1024*1024){
            fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
        }
        else{
            fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';
        }
        var name = file.name;
        var type = file.type;
    }
}
