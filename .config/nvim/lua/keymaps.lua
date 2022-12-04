function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

local keys = {
				n={
								{'<A-g>',':NvimTreeToggle<cr>'},
								{ 'yf', ":let @+=expand('%:p')<CR>", {silent=true}}, -- copies filepath to clipboardng 
								{ 'yd', ":let @+=expand('%:p:h')<CR>", {silent=true}}, -- copies dirpath to clipboardng
								{'gf', ':vert winc f<cr>'} -- opens file below cursor 
				}
}


-- ~/.config/nvim/lua/basic.lua

for k, v in pairs(keys) do
				for n, a in pairs(v) do
								if #a == 2 then 
												vim.keymap.set(k,a[1],a[2])
								elseif #a>2 then 
												vim.keymap.set(k,a[1],a[2],a[3])
								end
				end
end
