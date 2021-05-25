
var code;Vue.component('w-example',{props:{lang:{type:String,default:'html'},isResult:{type:Boolean,default:true},isBase:{type:Boolean,default:true}},data(){return{id:null,active:false,hasMoved:false,percent:40,darkMode:false,horizontalMode:true,sandbox:{'html':'','css':'','js':'','title':'','descr':''}}},mounted(){var html=this.$slots.default[0].text;var doctype=html.toLowerCase().indexOf('<!doctype');if(doctype==-1){code='<!DOCTYPE html><html><head><meta charset="utf-8"><title>webref.ru</title>';if(this.$props.isBase==true)code+='<base target="_blank" href="/example/">';code+='</head><body>'+html+'</body></html>';}else{if(this.$props.isBase==true)code=html.replace('</head>','<base href="/example/" target="_blank"></head>');else code=html;}
if(this.$props.lang!='html'){this.$props.isResult=false;}
if(this.$props.isResult==true){let result=this.$refs.result.contentWindow;result.document.write(code);result.document.close();}
this.id=this._uid;this.sandbox=sandbox(code);if(localStorage.darkMode){this.darkMode=localStorage.darkMode==='true';}
if(localStorage.horizontalMode){this.horizontalMode=localStorage.horizontalMode==='true';}
this.percent=(this.horizontalMode===true&&this.$props.isResult===true)?40:100;},watch:{darkMode:function(){localStorage.darkMode=this.darkMode;}},methods:{reloadExample:function(){let result=this.$refs.result.contentWindow;result.document.open();result.document.write(code);result.document.close();},splitMode:function(){this.horizontalMode=!this.horizontalMode;localStorage.horizontalMode=this.horizontalMode;this.percent=(this.horizontalMode===true)?40:100;},newTab:function(){this.$refs.webref.submit();},copyCode(){let range=document.createRange();range.selectNodeContents(document.querySelector('.w-example-code'));window.getSelection().removeAllRanges();window.getSelection().addRange(range);document.execCommand('copy');},jsFiddle:function(){this.$refs.jsFiddle.submit();},codePen:function(){this.$refs.codePen.submit();},onMouseDown(){this.active=true;this.hasMoved=false;},onMouseUp(){this.active=false;},onMouseMove(e){if(e.buttons===0||e.which===0){this.active=false}
if(this.active){let offset=0
let target=e.currentTarget;while(target){offset+=target.offsetLeft;target=target.offsetParent;}
const currentPage=e.pageX;const targetOffset=e.currentTarget.offsetWidth;const percent=Math.floor(((currentPage-offset)/targetOffset)*10000)/100
if(percent>20&&percent<80){this.percent=percent;}
this.$emit('resize',this.percent)
this.hasMoved=true}},},computed:{userSelect(){return this.active?'none':'';},},template:`<div class="w-example">
<div class="w-example-toolbar" v-if="isResult==true">
<div class="is-pulled-left">
<span><input :id="id" type="checkbox" class="switch" v-model="darkMode"><label :for="id">Тёмная тема</label></span>
</div>
<div class="is-pulled-right">
<span @click="reloadExample" title="Обновить результат"><i class="icon-play"></i></span>
<span @click="splitMode"><i :class="horizontalMode==true ? 'icon-vertical-split' : 'icon-horizontal-split'"></i></span>
<span @click="newTab" title="Открыть в новой вкладке"><i class="icon-popup"></i></span>
<form action="/example/" method="post" target="_blank" ref="webref" hidden><input type="hidden" name="codetext" :value="code"></form>
<span @click="copyCode" title="Скопировать код в буфер"><i class="icon-copy"></i></span>
<span @click="jsFiddle" title="Открыть в JSFiddle"><i class="icon-jsfiddle"></i></span>
<form action="https://jsfiddle.net/api/post/library/pure/" method="post" target="_blank" ref="jsFiddle" hidden><input type="hidden" name="title" :value="sandbox.title"><input type="hidden" name="description" :value="sandbox.descr"><input type="hidden" name="html" :value="sandbox.html"><input type="hidden" name="css" :value="sandbox.css"><input type="hidden" name="js" :value="sandbox.js"></form>
<span @click="codePen" title="Открыть в CodePen"><i class="icon-codepen"></i></span>
<form action="https://codepen.io/pen/define" method="post" target="_blank" ref="codePen" hidden><input type="hidden" name="data" :value="sandbox.codepen"></form>
</div>
</div>
<div class="multipane" :class="horizontalMode==true ? 'multipane-horizontal' : 'multipane-vertical'" :style="userSelect" @mouseup="onMouseUp" @mousemove="onMouseMove">
<div class="pane pane-mobile" :class="isResult==true ? 'pane-l-desktop' : 'pane-l-mobile'" :style="{ width: percent+'%'}">
<pre :class="darkMode==true? 'theme-dark' : 'theme-light'"><code :data-language="lang" ref="source" class="w-example-code"><slot></slot></code></pre>
</div>
<div class="multipane-resizer" v-if="isResult==true && horizontalMode==true" @mousedown="onMouseDown"></div>
<div class="pane pane-r-desktop pane-mobile" v-if="isResult==true">
<iframe class="w-example-result" ref="result"></iframe>
</div>
</div>
</div>`});Vue.component('w-individual',{data(){return{isShowing:false}},computed:{buttonValue:function(){return(this.isShowing)?'Скрыть ответ':'Показать ответ';}},template:`<section class="individual-result">
	<p><button class="button is-info is-outlined" @click="isShowing=!isShowing">{{ buttonValue }}</button></p>
<div class="individual-answer" v-show="isShowing">
<slot></slot>
</div>
</section>`});Vue.component('b-tabs',{props:{value:Number,type:{type:String,default:'is-boxed'}},data(){return{activeTab:this.value||0,tabs:[]}},created(){this.tabs=this.$children;},methods:{selectTab:function(selectedTab){this.tabs.forEach(tab=>{tab.isActive=(tab.label==selectedTab.label);});},activeTab:function(selectedTab){this.tabs[selectedTab].isActive=true;}},mounted(){this.tabs[this.activeTab].isActive=true;},template:`<div class="b-tabs">
<nav class="tabs" :class="type">
	<ul>
		<li v-for="tab in tabs" :class="{ 'is-active': tab.isActive }">
			<a @click="selectTab(tab)"><span v-if="tab.icon" class="icon"><i class="icon" :class="tab.icon"></i></span><span>{{ tab.label }}</span></a>
		</li>
	</ul>
</nav>
<section class="tab-content">
	<slot></slot>
</section>
</div>`});Vue.component('b-tab-item',{props:{label:{type:String,required:true},icon:{type:String,}},template:`<div class="tab-item" :class="{ 'is-active': isActive }"><slot></slot></div>`,data(){return{isActive:false}}});function sandbox(code){var data={'html':'','css':'','js':'','title':'','descr':'','codepen':''};var title,css,js,html;title=code.match("<title>(.*)<\/title>");css=code.match("<style[^>]*>((?:.|\r?\n)*?)<\/style>");js=code.match("<script>((?:.|\r?\n)*?)</script>");html=code.match("<body[^>]*>((?:.|\r?\n)*?)<\/body>");if(!!html){var img=new RegExp('<img src="image/','g');data.html=html[1].replace(img,'<img src="//webref.ru/example/image/');}
if(!!css){var img=new RegExp('url\\(/example/image/','g');data.css=css[1].replace(img,'url(//webref.ru/example/image/');}
if(!!js)data.js=js[1];if(!!title)data.title=title[1];data.descr=window.location.href;codepen={'title':data.title,'description':data.descr,'html':data.html,'css':data.css,'js':data.js};data.codepen=JSON.stringify(codepen);return data;}
Vue.component('w-practice',{props:{script:{type:String,required:true},nextId:{type:Number,default:0},},data(){return{task:this.$props.script,correct:[],animated:[],nextId:this.$props.nextId}},methods:{run:function(){practiceResult();},check:function(){practiceResult();for(i=0;i<numTask;i++){if(mTypeTask[i]=="html")Vue.set(this.correct,i,this.testCode(userHTML,mAssert[i]));else if(mTypeTask[i]=="css")Vue.set(this.correct,i,this.testCode(userCSS,mAssert[i]));Vue.set(this.animated,i,!this.correct[i]);}
validateTask();},testCode:function(testString,patternString){patternString=patternString.replace(/(\s+)/gm,"");testString=testString.replace(/(\r\n|\n|\r|\s+)/gm,"");var re=new RegExp(patternString,'i');return re.test(testString);},removeShake:function(index){Vue.set(this.animated,index,false);},showSuccess(){var b=(nextId>0)?{cancel:"Закрыть",next:{text:"Следующая задача",value:"next"}}:{cancel:"Закрыть"};swal({icon:"success",title:"Поздравляем!",text:"Вы правильно выполнили задачу.",buttons:b,}).then((value)=>{if(value=="next"){document.location="/practice/"+nextId;}});}},mounted(){var self=this;console.log(self.$slots.css3[0].children[0])
this.$nextTick(function(){var disabled=self.task['disabled']||"";if(self.$slots.html5!=null){let readOnlyHTML=(disabled=="html")?"nocursor":false;let editorHTML=CodeMirror.fromTextArea(self.$slots.css3[0].children[0],{mode:'text/html',lineNumbers:true,readOnly:readOnlyHTML});}
if(self.$slots.css3!=null){let readOnlyCSS=(disabled=="css")?"nocursor":false;let editorCSS=CodeMirror.fromTextArea(self.$refs.css,{mode:'text/css',lineNumbers:true,readOnly:readOnlyCSS});}});},template:`<section class="w-practice">
	<div class="practice_task_area">
	<div v-for="(value, index) in task.task" :key="index" :class="[correct[index] ? 'success' : 'alert', {'shake': animated[index]}]" @animationend="removeShake(index)" class="practice_task callout" v-cloak>
		{{ value.string }}
	</div>
</div>
<div class="columns">
	<div class="column is-6">
		<div class="practice_toolbar"><button class="practice_run button is-link is-small" @click="run"><i class="icon-play"></i> Выполнить</button></div>       
    </div>
	<div class="column is-6">
		<div class="practice_toolbar is-right"><button class="practice_validate button is-link is-small" @click="check"><i class="icon-help"></i> Проверить</button></div>
    </div>
</div>
<div class="columns">
	<div class="column is-12-mobile is-6-desktop">
		<slot name="css3"></slot>
		<slot name="html5"></slot>
	</div>
	<div class="column is-12-mobile is-6-desktop">
		<div class="practice_browser"><iframe ref="result"></iframe></div>
	</div>
</div>
</section>`});var webrefMain=new Vue({el:"#webref-main",data:{isHintSyntax:false,isHintBrowser:false,isHintSpec:false,playgroundValue:''}});Vue.config.devtools=false;