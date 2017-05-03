#coding=utf-8

from django import forms

from .models import OutisPost
from .models import OutisComment

class PostForm(forms.ModelForm):
    class Meta:
        model = OutisPost
        fields = ['category_id', 'title', 'link', 'description', 'tag', 'attraction']


class OutisCommentForm(forms.ModelForm):
    class Meta:
        """指定一些 Meta 选项以改变 form 被渲染后的样式"""
        model = OutisComment # form 关联的 Model

        fields = ['content']

        widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 username 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'content': forms.Textarea(attrs={'placeholder': '评论'}),
        }
