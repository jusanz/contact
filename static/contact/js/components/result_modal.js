const result_modal = {
  data() {
    return {
      email: "",
      message: ""
    }
  },
  methods: {
    show(data){
      this.email = data.email;
      this.message = data.message;
      this.modal.show();
    }
  },
  mounted() {
      this.modal = new bootstrap.Modal(this.$refs.modal, {})
  },
  template: `
    <div ref="modal" class="modal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body p-5">
            <h2 class="fw-bold mb-0">下記お問い合わせを受け付けました</h2>
            <ul class="d-grid gap-4 my-5 list-unstyled">
              <li class="d-flex gap-4">
                <div>
                  <h5>{{ email }} 様</h5>
                  {{ message }}
                  <hr class="my-4">
                  この度はお問い合わせをいただき誠にありがとうございます。
                  管理人が内容を確認いたします。<br/>
                </div>
              </li>
            </ul>
          </div>
          <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  `
};