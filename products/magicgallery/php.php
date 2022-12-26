<?php

function productTable($name, $price, $descrip) {
?>
<table width="80%" border="1" align="center" cellpadding="5" cellspacing="5" bordercolor="#C6C6C6" class="prodTable">
  <tr>
    <th width="15%" scope="row"><div align="right">Name:</div></th>
    <td><?php echo $name ?></td>
    <th width="10%"><div align="right">Price:</div></th>
    <td width="10%"><?php echo $price ?></td>
  </tr>
  <tr>
    <th width="20%" scope="row"><div align="right">Description:</div></th>
    <td colspan="3" rowspan="2"><?php echo $descrip ?></td>
  </tr>
  <tr>
    <th width="20%" scope="row"><div align="right"></div></th>
  </tr>
</table>
<?php
} // end productTable()
?>