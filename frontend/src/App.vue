<template>  
  
  <!-- 入力フォームと生成ボタン -->
  <div>
    <h2 class="mt-5 text-center">メール作成フォーム</h2>
    <p class="mb-4 text-center">▼メールの詳細を入力してください▼</p>
    <div class="mb-3">
      <textarea v-model="Message" class="form-control" placeholder="メールの内容" rows="5"></textarea>
    </div>
    <button v-on:click="Generate" class="btn btn-primary btn-lg w-100">生成</button>
  </div> 

  <!-- ローディング中の表示 -->
  <div v-if="status === 'pending'" class="mt-3">
    <p class="alert alert-dark d-flex align-items-center">
      <div class="spinner-border me-2 text-dark" role="status"></div>
      メールを生成しています
    </p>
  </div>

  <!-- 失敗時の表示 -->
  <p v-if="status === 'fail'" class="alert alert-danger mt-3">
    メールの生成に失敗しました: {{ errorMsg }}
  </p>

  <!-- 成功時の表示 -->
  <template v-if="status === 'success'">

    <!-- cardの表示 -->
    <div class="card mt-5">

      <!-- cardのheader表示 -->
      <div class="card-header pt-3">
        <div class="row align-items-center">
          <!-- 件名の表示 -->
          <div class="col">
            <h5 class="ditable-code-title card-title" contenteditable="true">
              {{ subject }}
            </h5>
          </div>
          <!-- コピーアイコンの表示 -->
          <div class="w-25">
            <template v-if="!titleClip">
              <button class="btn btn-outline-dark float-end" @click="copyToClipboard(subject, 'title')">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">
                  <path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/>
                  <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/>
                </svg>
              </button>
            </template>
            <template v-else>
              <button class="btn btn-outline-dark float-end">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                  <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
                </svg>
              </button>
            </template>
          </div>
        </div>
      </div>

      <!-- cardのbody表示 -->
      <div class="card-body">

        <!-- コピーアイコンの表示 -->
        <div>
          <div class="float-end" v-if="!bodyClip">
            <button class="btn btn-outline-dark float-end mb-3" @click="copyToClipboard(modified_content, 'body')">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">
                <path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/>
                <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/>
              </svg>
            </button>
          </div>
          <div class="float-end"  v-else>
            <button class="btn btn-outline-dark float-end mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg>
            </button>  
          </div>
        </div>

        <!-- テキストエリアの表示 -->
        <textarea class="editable-code-body w-100 my-3" rows="10">
          {{ modified_content }}
        </textarea>

      </div>

    </div>

    

  </template>
  <br><br><br><br>

</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      Message: "",
      subject: "",
      modified_content: "",
      status: "",
      errorMsg: "",
      titleClip: false,
      bodyClip: false,
    };
  },
  methods: {
    Generate() {
      if (!this.Message) {
        this.errorMsg = "メールの内容を入力してください"
        this.status = "fail"
        // alert('全ての項目を入力してください');
        return;
      }
      else{
        this.status = "pending"

        const dataToSend = {        
          content: this.Message
        };

        axios.post('http://127.0.0.1:8080/', dataToSend,{
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            })
            .then(response => {
              this.status = "success"
              const data = response.data
              console.log(data.detail)
              if (data.status === "success"){
                this.subject = data.detail.subject
                this.modified_content = data.detail.modified_content
              }
              else{
                this.status = "fail"
                this.errorMsg = "サーバーの処理でERRORが発生しました"
              }

            })
            .catch(error => {
              this.status = "fail"
              console.error(error);
            });
      }
    },
    async copyToClipboard(input, content) {
      await navigator.clipboard.writeText(input)
      if (content === "title"){
        this.titleClip = true
        this.$nextTick(() => {
          setTimeout(() => {
            this.titleClip = false;
          }, 3000);
        });
      }else if(content === "body"){
        this.bodyClip = true
        this.$nextTick(() => {
          setTimeout(() => {
            this.bodyClip = false;
          }, 3000);
        });
      }
      
    }
  }
};
</script>


<style scoped>
/* card-headerのデザイン */
.editable-code-title {
            display: block;
            border: none;
            padding: 20px;
            font-size: 16px;
            line-height: 1.5;
            resize: none; /* ユーザによるリサイズを無効にする */
        }

/* card-bodyのデザイン */
.editable-code-body {
    display: block;
    width: 80%; /* 調整可能な幅 */
    background-color: #f8f8f8;
    border: none;
    padding: 20px;
    font-size: 16px;
    line-height: 1.5;
    resize: none; /* ユーザによるリサイズを無効にする */
}
</style>