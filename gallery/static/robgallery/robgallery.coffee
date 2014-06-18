###
  RobGallery - Plugin Jquery desenvolvido para aplicação de galeria de imagens,
  desenvolvido especialmente para a equipe da Globo.com

  Por Jonhnatha Trigueiro <joepreludian@gmail.com>

  18/06/2014
###

$.fn.robgallery = () ->

  elements = []
  self = this

  photo_index =
    current: -1
    last: (this.children('li').length - 1)


  reached_end = (index_amount) ->
    next_item_index = photo_index.current + index_amount

    if next_item_index >= photo_index.last
      right_button.fadeTo 200, 0.1
    else
      right_button.fadeTo 200, 1

    if next_item_index <= 0
        left_button.fadeTo 200, 0.1
      else
        left_button.fadeTo 200, 1

    if photo_item[next_item_index] == undefined
      return true
    else
      return false

  update_counter = () ->

    current_photo_no = photo_index.current + 1
    total_photo_no = photo_index.last + 1

    photo_item.children('span[class=counter]',0).html "#{current_photo_no} de #{total_photo_no}"

  change_element = (index_amount) ->

    if !reached_end(index_amount)

      item = photo_item[photo_index.current]
      $(item).css 'display', 'none'

      photo_index.current += index_amount
      item = photo_item[photo_index.current]
      $(item).fadeTo 500, 1

      update_counter()


  this.children('li').addClass 'item'
  this.children('li').append '<span class=counter>'

  photo_item = this.children('li[class=item]')

  this.addClass 'robgallery'

  this.prepend '<li class="left">'
  this.append '<li class="right">'

  left_button = this.children('li[class=left]',0)
  left_button.on 'click', ()->
    change_element -1

  right_button = this.children('li[class=right]',0)
  right_button.on 'click', ()->
    change_element 1

  change_element 1