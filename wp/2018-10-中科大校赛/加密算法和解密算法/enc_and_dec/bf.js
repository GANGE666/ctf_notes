/* author: @ustc_zzzz */ class BF {
  constructor (write, read) {
    this.write = write || (o => 0 * setTimeout(console.log, 0, o) || (i => o.push(i)))([])
    this.read = read || (() => 0)
    this.pointer = 0
    this.data = []
    this.ops = {
      '>': (pointer, _) => {
        ++this.pointer
        return pointer
      },
      '<': (pointer, _) => {
        --this.pointer
        return pointer
      },
      ',': (pointer, _) => {
        this.data[this.pointer] = this.read()
        return pointer
      },
      '.': (pointer, _) => {
        let normalize = i => i < 0 ? i % 256 + 256 : i % 256
        this.write(normalize(this.data[this.pointer] || 0))
        return pointer
      },
      '+': (pointer, _) => {
        this.data[this.pointer] = (this.data[this.pointer] || 0) + 1
        return pointer
      },
      '-': (pointer, _) => {
        this.data[this.pointer] = (this.data[this.pointer] || 0) - 1
        return pointer
      },
      ']': (pointer, text) => {
        if ((this.data[this.pointer] || 0) % 256 === 0) return pointer
        for (let stack = 0; pointer >= 0; --pointer) {
          let char = text[pointer]
          if (char === '[') --stack
          if (char === ']') ++stack
          if (stack === 0) return pointer
        }
        throw new Error('Mismatched brackets in the program!')
      },
      '[': (pointer, text) => {
        if ((this.data[this.pointer] || 0) % 256 !== 0) return pointer
        for (let stack = 0; pointer < text.length; ++pointer) {
          let char = text[pointer]
          if (char === '[') ++stack
          if (char === ']') --stack
          if (stack === 0) return pointer
        }
        throw new Error('Mismatched brackets in the program!')
      }
    }
  }

  run (text) {
    for (let pointer = 0; pointer < text.length; ++pointer) {
      let op = this.ops[text[pointer]]
      pointer = op ? op(pointer, text) : pointer
    }
    return this
  }
}
