var koma_id = document.getElementById('koma_id').value;

var app = new Vue({
  el: '#annotate',
  delimiters: ["[[", "]]"],
  data: {
    char_num: 1,
    have_eyes_num: 1,
    koma_id: '',
    whos_str: '',
    grad_str: '',
    eyes_str: '',
    step: 1,
    grad_list: ['左向き前', '右向き前', '正面前', '背面'],
  },
  mounted: function () {
    this.koma_id = koma_id
    this.char_num = document.getElementById("chara_num").value
    this.whos_str = document.getElementById("whos").value
    this.grad_str = document.getElementById("face_direction").value
    this.eyes_str = document.getElementById("eyes").value
    this.step = document.getElementById("step").value
  },
  computed: {
    is_can_save: function() {
      // 簡単なバリデーション
      var is_fill_whos_and_grad = this.whos_str !== '' && this.grad_str !== ''
      var is_eyes_input_ok = (this.get_have_eyes_num() > 0 && this.eyes_str !== '') || this.get_have_eyes_num() === 0
      const is_ok_inputed_str = is_fill_whos_and_grad && is_eyes_input_ok

      var is_equall_chara_num_and_whos_len = Number(this.char_num) === this.whos_str.split(',').length - 1
      var is_equall_grad_str_len_and_grad_str_len = this.have_eyes_num === this.eyes_str.split(',').length - 1
      const is_ok_str_length = is_equall_chara_num_and_whos_len && is_equall_grad_str_len_and_grad_str_len

      return is_ok_inputed_str && is_ok_str_length
    },
    int_char_num: function () {
      return Number(this.char_num)
    },
  },
  filters: {
    captionFormat: function (date) {
      var id_split = this.koma_id.split('-')
      return `${id_split[0]}巻${id_split[1]}ページ${id_split[2]}コマ目`
    }
  },
  methods: {
    get_have_eyes_num: function(){
      var ches = document.querySelectorAll("[type=radio]:checked")
      var have_eyes_num = 0
      for (var i=0; i< ches.length; i++) {
        var label_text = ches[i].labels[0].innerText
        label_text.indexOf('前') > 0 ? have_eyes_num++ : null
      }
      return have_eyes_num
    },
    send_who_str: function (elem) {
      var value = elem.target.labels[0].innerText
      if (value && value.length == 1){
        this.whos_str = this.whos_str + value + ','
      }
    },
    send_grad_or_eyes_str: function (kind) {
      var ches = document.querySelectorAll("[type=radio]:checked")
      var target_str = ''
      for (var i=0; i< ches.length; i++) {
        if(ches[i].id.indexOf(kind) > 0){
          var label_text = ches[i].labels[0].innerText
          target_str = target_str + label_text + ','
        }
      }
      if (kind == 'grad') {
        this.grad_str = target_str
      } else if (kind == 'eyes') {
        this.eyes_str = target_str
      }
    },
    change_eyes_num: function () {
      this.have_eyes_num = this.get_have_eyes_num()
      this.send_grad_or_eyes_str('grad')
    },
    reset_values: function () {
      this.char_num=1
      this.have_eyes_num=1
      this.koma_id=''
      this.whos_str=''
      this.grad_str=''
      this.eyes_str=''
    },
  }
})