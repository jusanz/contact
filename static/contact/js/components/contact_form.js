const contact_form = {
  props:["url"],
  data() {
    return {
      email: "",
      message: "",
      invalid_email: "",
      invalid_message: "",
    }
  },
  methods: {
    _post: async function (url, data) {
      await axios.post(url, data)
        .then((response) => {
        })
        .catch((error) => {
          alert(error)
        });
    },
    post() {
      this._post(this.url,
        {
          json: {
            email: this.email,
            message: this.message
          },
        }).then(() => {
          const data = {
            email: this.email,
            message: this.message
          };
          this.$emit("created", data);
          this.email = "";
          this.message = "";
        })
    },
    _validateEmail(email) {
      return String(email)
        .toLowerCase()
        .match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
    },
    submit() {
      this.invalid_email = "";
      this.invalid_message = "";

      if (!this._validateEmail(this.email)) {
        this.invalid_email = "有効なメールアドレスを入力してください";
        this.$refs.email.scrollIntoView({ behavior: "smooth" });
        this.$refs.email.focus();
        return
      }
      if (!this.message) {
        this.invalid_message = "お問い合わせ内容を入力してください";
        this.$refs.message.scrollIntoView({ behavior: "smooth" });
        this.$refs.message.focus();
        return
      }
      this.post();
    }
  },
  template: `
      <form @submit.prevent="submit">
        <div class="row g-3">

          <div class="col-12">
            <label class="form-label">メールアドレス</label>
            <input ref="email" type="email" class="form-control" placeholder="メールアドレスを入力してください" v-model="email">
            <div v-if="invalid_email" class="alert alert-danger" role="alert">
              {{ invalid_email }}
            </div>
          </div>

          <div class="col-12">
            <label class="form-label">お問い合わせ内容</label>
            <textarea ref="message" class="form-control" rows="10" v-model="message"></textarea>
            <div v-if="invalid_message" class="alert alert-danger" role="alert">
              {{ invalid_message }}
            </div>
          </div>

        </div>

        <hr class="my-4">

        <button class="w-100 btn btn-outline-dark btn-lg" type="submit">送信する</button>
      </form>
  `
};