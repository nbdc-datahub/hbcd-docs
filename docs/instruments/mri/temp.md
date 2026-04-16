<table class="compact-table-no-vertical-lines" style="width: 100%; table-layout: fixed;">
<thead>
    <tr>
    <th style="text-align: center;"><a href="#qsirecon-DIPYDKI">qsirecon-DIPYDKI</a></th>
    <th>Model</th>
    <th>Parameter</th>
    <th>Description</th>
    <th>Shells</th>
    </tr>
</thead>
<tbody>
<tr><td></td><td>dki</td><td>ad</td><td>Axial diffusivity</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>ak</td><td>Axial kurtosis</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>fa</td><td>Fractional anisotropy</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>kfa</td><td>Kurtosis fractional anisotropy</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>md</td><td>Mean diffusivity</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>mk</td><td>Mean kurtosis</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>mkt</td><td>Mean kurtosis tensor</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>rd</td><td>Radial diffusivity</td><td>Full</td></tr>
<tr><td></td><td>dki</td><td>rk</td><td>Radial kurtosis</td><td>Full</td></tr>
<thead>
<tr><td colspan="5"></td></tr>
    <tr>
    <th style="text-align: center;"><a href="#qsirecon-TORTOISE">qsirecon-TORTOISE_model-MAPMRI</a></th>
    <th>Model</th>
    <th>Parameter</th>
    <th>Description</th>
    <th>Shells</th>
    </tr>
</thead>
<tr>
<tr><td></td><td>mapmri</td><td>ng</td><td>Non-Gaussianity</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>ngpar</td><td>Non-Gaussianity parallel</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>ngperp</td><td>Non-Gaussianity perpendicular</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>pa</td><td>Propagator anisotropy</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>path</td><td>Thresholded propagator anisotropy</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>rtap</td><td>Return to axis probability</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>rtop</td><td>Return to origin probability</td><td>Full</td></tr>
<tr><td></td><td>mapmri</td><td>rtpp</td><td>Return to plane probability</td><td>Full</td></tr>
<tr><td></td><td>tensor</td><td>ad</td><td>Axial diffusivity</td><td>Inner</td></tr>
<tr><td></td><td>tensor</td><td>am</td><td>A0 from a tensor fit</td><td>Inner</td></tr>
<tr><td></td><td>tensor</td><td>fa</td><td>Fractional anisotropy from a tensor fit</td><td>Inner</td></tr>
<tr><td></td><td>tensor</td><td>li</td><td>Lattice index</td><td>Inner</td></tr>
<tr><td></td><td>tensor</td><td>rd</td><td>Radial diffusivity from a tensor fit</td><td>Inner</td></tr>
<thead>
<tr><td colspan="5"></td></tr>
    <tr>
    <th style="text-align: center;"><a href="#qsirecon-TORTOISE">qsirecon-TORTOISE_model-tensor</a></th>
    <th>Model</th>
    <th>Parameter</th>
    <th>Description</th>
    <th>Shells</th>
    </tr>
</thead>
<tr>
<tr><td></td><td>tensor</td><td>ad</td><td>Axial diffusivity</td><td>Full</td></tr>
<tr><td></td><td>tensor</td><td>am</td><td>A0 from a tensor fit</td><td>Full</td></tr>
<tr><td></td><td>tensor</td><td>fa</td><td>Fractional anisotropy from a tensor fit</td><td>Full</td></tr>
<tr><td></td><td>tensor</td><td>li</td><td>Lattice index</td><td>Full</td></tr>
<tr><td></td><td>tensor</td><td>rd</td><td>Radial diffusivity from a tensor fit</td><td>Full</td></tr>
</tbody>
</table>


## NEW

<table class="compact-table-no-vertical-lines" style="width: 100%; table-layout: fixed;">
<thead>
<tr>
<th>Pipeline</th>
<th>Model</th>
<th>Parameters</th>
<th>Description</th>
<th>Shells</th>
</tr>
</thead>
<tbody>

<!-- DIPY DKI -->
<tr class="table-section">
<td colspan="5"><b><a href="#qsirecon-DIPYDKI">qsirecon-DIPYDKI</a></b></td>
</tr>

<tr>
<td></td>
<td rowspan="2"><b>dki</b></td>
<td><code>fa, md, rd, ad</code></td>
<td>Standard diffusion metrics</td>
<td rowspan="2">Full</td>
</tr>
<tr>
<td></td>
<td><code>mk, rk, ak, kfa, mkt</code></td>
<td>Kurtosis-based metrics</td>
</tr>

<!-- TORTOISE MAPMRI -->
<tr class="table-section">
<td colspan="5"><b><a href="#qsirecon-TORTOISE">qsirecon-TORTOISE (MAP-MRI)</a></b></td>
</tr>

<tr>
<td></td>
<td rowspan="2"><b>mapmri</b></td>
<td><code>rtop, rtap, rtpp</code></td>
<td>Return-to-probability metrics</td>
<td rowspan="2">Full</td>
</tr>
<tr>
<td></td>
<td><code>ng, ngpar, ngperp, pa, path</code></td>
<td>Non-Gaussianity and anisotropy metrics</td>
</tr>

<tr>
<td></td>
<td><b>tensor</b></td>
<td><code>fa, rd, ad, am, li</code></td>
<td>Tensor-derived measures</td>
<td>Inner</td>
</tr>

<!-- TORTOISE TENSOR -->
<tr class="table-section">
<td colspan="5"><b><a href="#qsirecon-TORTOISE">qsirecon-TORTOISE (Tensor)</a></b></td>
</tr>

<tr>
<td></td>
<td><b>tensor</b></td>
<td><code>fa, rd, ad, am, li</code></td>
<td>Tensor-derived measures</td>
<td>Full</td>
</tr>

</tbody>
</table>