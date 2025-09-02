# Child Demographics Branching Logic

#### Sex at Birth
<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 5%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c299;">
<td>1</td>
<td>Sex at Birth</td>
<td>N/A (calculated field)</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>

#### Race & Ethnicity
<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 5%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c299;">
    <td><strong>2</strong></td>
    <td colspan="2"><strong>Race/ Ethnicity <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
<td>3</td>
<td style="word-wrap: break-word; white-space: normal;">Which categories describe your child? Select all that apply. Note, you may select more than one group.</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, American Indian or Alaska Native | 1, Asian | 2, Black, African American, or African | 3, Hispanic, Latino, or Spanish | 4, Middle Eastern or North African | 5, Native Hawaiian or other Pacific Islander | 6, White | 7, None of these fully describe me / Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>4</td>
<td>American Indian or Alaska Native</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, American Indian | 1, Alaska Native | 2, Central or South American Indian | 3, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=0</td>
</tr>
<tr>
<td>5</td>
<td>Asian</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, Asian Indian | 1, Cambodian | 2, Chinese | 3, Filipino | 4, Hmong | 5, Japanese | 6, Korean | 7, Pakistani | 8, Vietnamese | 9, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=1</td>
</tr>
<tr>
<td>6</td>
<td>Black, African American, or African</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, African American | 1, Barbadian | 2, Caribbean | 3, Ethiopian | 4, Ghanaian | 5, Haitian | 6, Jamaican | 7, Liberian | 8, Nigerian | 9, Somali | 10, South African | 11, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=2</td>
</tr>
<tr>
<td>7</td>
<td>Hispanic, Latino, or Spanish</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, Colombian | 1, Cuban | 2, Dominican | 3, Ecuadorian | 4, Honduran | 5, Mexican or Mexican American | 6, Puerto Rican | 7, Salvadoran | 8, Spanish | 9, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=3</td>
</tr>
<tr>
<td>8</td>
<td>Middle Eastern or North African</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, Afghan | 1, Algerian | 2, Egyptian | 3, Iranian | 4, Iraqi | 5, Israeli | 6, Lebanese | 7, Moroccan | 8, Syrian | 9, Tunisian | 10, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=4</td>
</tr>
<tr>
<td>9</td>
<td>Native Hawaiian or other Pacific Islander</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, Chamorro | 1, Chuukese | 2, Fijian | 3, Marshallese | 4, Native Hawaiian | 5, Palauan | 6, Samoan | 7, Tahitian | 8, Tongan | 9, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=4</td>
</tr>
<tr>
<td>10</td>
<td>White</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">0, Dutch | 1, English | 2, European | 3, French | 4, German | 5, Irish | 6, Italian | 7, Norwegian | 8, Polish | 9, Scottish | 10, Spanish | 11, None of these fully describe me/Other | 999, Don't know | 777, Decline to answer</span></span></td>
<td>3=6</td>
</tr>
<tr>
<td>11</td>
<td style="word-wrap: break-word; white-space: normal;">How do other people usually classify your child in this country? Select all that apply. Note, you may select more than one group.</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-top"><i>Hover for options</i><span class="tooltiptext" style="width: 300px;">1, American Indian or Alaska Native | 2, Asian | 3, Black, African American, or African | 4, Hispanic, Latino, or Spanish | 5, Middle Eastern or North African | 6, Native Hawaiian or other Pacific Islander | 7, White | 8, None of these fully describe me | 999, Don't know | 777, Decline to answer</span></span></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>

#### Relationship & Living with the Child

<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 5%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c2ff; border-top: 2px solid #c4c2c2ff;">
    <td><strong>12</strong></td>
    <td colspan="2"><strong>Relationship with the Child <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
    <td>13</td>
    <td>What is the child's relationship to you?</td>
    <td style="word-wrap: break-word; white-space: normal;">1, Child | 2, Foster Child | 3, Grandchild | 4, Sibling | 5, Other family member | 6, Non-family (a friend or friend of the family) | 7, Other</td>
    <td>&nbsp;</td>
</tr>
<tr>
    <td><strong>14</strong></td>
    <td colspan="2"><strong>Living with the Child <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
<td>15</td>
<td>Do you live with the child?</td>
<td>0, No | 1, Yes</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>16</td>
<td style="word-wrap: break-word; white-space: normal;">How many days per month do you live with the child?</td>
<td>1, 1 | ... | 30, 30</td>
<td>15=1</td>
</tr>
</tbody>
</table>


#### Child Custody

<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 5%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c2ff;">
    <td><strong>17</strong></td>
    <td colspan="2"><strong>Child Custody <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
<td>18</td>
<td style="word-wrap: break-word; white-space: normal;">Are you the child's legal guardian</td>
<td>0, No | 1, Yes</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>19</td>
<td style="word-wrap: break-word; white-space: normal;">Aside from yourself, is there another adult in the household who is responsible for child's health, education and well-being?</td>
<td>0, No | 1, Yes</td>
<td>if 18 = 0</td>
</tr>
<tr>
<td>20</td>
<td style="word-wrap: break-word; white-space: normal;">Is that other caregiver the child's legal guardian?</td>
<td>0, No | 1, Yes</td>
<td>if 19 = 1</td>
</tr>
<tr>
<td>21</td>
<td style="word-wrap: break-word; white-space: normal;">Does the child have a legal guardian living in the household?</td>
<td>0, No | 1, Yes</td>
<td>if 20 = 0</td>
</tr>
<tr>
<td>22</td>
<td style="word-wrap: break-word; white-space: normal;">Who is the child&rsquo;s legal guardian?</td>
<td style="word-wrap: break-word; white-space: normal;">1, Parent | 2, State foster care system | 3, Grandparent | 4, Sibling | 5, Other family | 6, Non-family (friend, or friend of the family) | 7, Other</td>
<td>if 21 = 0</td>
</tr>
<tr>
<td>19</td>
<td style="word-wrap: break-word; white-space: normal;">Aside from yourself, is there another adult in the household who is responsible for child's health, education and well-being?</td>
<td>0, No | 1, Yes</td>
<td>if 18 = 0</td>
</tr>
<tr>
<td>20</td>
<td style="word-wrap: break-word; white-space: normal;">Is that other caregiver the child's legal guardian?</td>
<td>0, No | 1, Yes</td>
<td>if 19 = 1</td>
</tr>
<tr>
<td>21</td>
<td style="word-wrap: break-word; white-space: normal;">Does the child have a legal guardian living in the household?</td>
<td>0, No | 1, Yes</td>
<td>if 20 = 0</td>
</tr>
<tr>
<td>22</td>
<td style="word-wrap: break-word; white-space: normal;">Who is the child's legal guardian?</td>
<td style="word-wrap: break-word; white-space: normal;">1, Parent | 2, State foster care system | 3, Grandparent | 4, Sibling | 5, Other family | 6, Non-family (friend, or friend of the family) | 7, Other</td>
<td>if 21 = 0</td>
</tr>
</tbody>
</table>

#### Household Relationships

<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 5%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c2ff;">
    <td><strong>23</strong></td>
    <td colspan="2"><strong>Household Relationships <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
    <td>24</td>
    <td colspan="2" style="word-wrap: break-word; white-space: normal;">We would like to know more about your child&rsquo;s current living situation. This includes the child&rsquo;s household (the group of people who live with the child) and where the child lives (a home, dwelling, or place). Please include any places where your child lives for at least 2 days per week.</td>
    <td></td>
</tr>
<tr>
<td>25</td>
<td style="word-wrap: break-word; white-space: normal;">How many households does your child live in for at least two nights per week?</td>
<td style="word-wrap: break-word; white-space: normal;">1, 1 | 2, 2 | 3, 3</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>

#### Household-Specific Details

<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 5%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c2ff;">
    <td><strong>26</strong></td>
    <td colspan="2"><strong>Household 1 <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
<td>27</td>
<td style="word-wrap: break-word; white-space: normal;">How would you describe this household?</td>
<td style="word-wrap: break-word; white-space: normal;">1, Person private residence (own or rent) | 2, Residence of a relative or friend | 3, Treatment facility | 4, Shelter | 5, No primary residence | 6, Other</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>28</td>
<td style="word-wrap: break-word; white-space: normal;">How many rooms are in the house? Please include bedrooms, kitchen, dining rooms, living rooms, family rooms, finished basements, and finished attics. Please exclude bathrooms and porches.</td>
<td style="word-wrap: break-word; white-space: normal;">1, 1 | 2, 2 | ... 10, 10 or more</td>
<td style="word-wrap: break-word; white-space: normal;">31 = 1, 2, or 6</td>
</tr>
<tr>
<td>29</td>
<td colspan="2" style="word-wrap: break-word; white-space: normal;">Excluding the child, how many people live in the child&rsquo;s household? If you live with the child in a household, please make sure to include yourself. Provide these details for both a first and second household, if applicable. If the child lives in 3 or more households, please answer for the two the child spends the most time in.</td>
<td>32 = 1, 2, or 6</td>
</tr>
<tr>
<td>30</td>
<td style="word-wrap: break-word; white-space: normal;">Number of adults (18 years of age or older)</td>
<td style="word-wrap: break-word; white-space: normal;">1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 or more</td>
<td>31 = 1, 2, or 6</td>
</tr>
<tr>
<td>31</td>
<td style="word-wrap: break-word; white-space: normal;">Number of children (17 years of age or younger)</td>
<td style="word-wrap: break-word; white-space: normal;">0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 or more</td>
<td>31 = 1, 2, or 6</td>
</tr>
<tr>
<td>32</td>
<td style="word-wrap: break-word; white-space: normal;">Total number in household</td>
<td style="word-wrap: break-word; white-space: normal;">Add answer 28 + 29 <i>(calculated field)</i></td>
<td>31 = 1, 2, or 6</td>
</tr>
<tr>
    <td>33</td>
    <td colspan="2" style="word-wrap: break-word; white-space: normal;">Please complete a row in the table below for each person&nbsp;who lives in the child's household at least two nights a week. Please start with yourself if you are the primary caregiver and living in this household. Continue to list from the youngest person to the oldest for up to 16 people.</td>
    <td>32 &gt; = 1</td>
</tr>
<tr>
    <td><strong>34 - 39</strong></td>
    <td colspan="2"><strong>Header rows for Person {1-16}</strong></td>
    <td><strong>32 &gt; = 1</strong></td>
</tr>
<tr>
    <td>40</td>
    <td>Person 1 Age Years</td>
    <td style="word-wrap: break-word; white-space: normal;">0, Less than 1 | 1, 1 | ... | 84, 84 | 85, 85 or more| 999, Don't know | 777, Decline to answer</td>
    <td>32 &gt; = 1</td>
</tr>
<tr>
<td>41</td>
<td>Person 1 Age Months</td>
<td style="word-wrap: break-word; white-space: normal;">0, Less than 1 | 1, 1 | 2, 2 | ... | 11, 11 | 999, Don't know | 777, Decline to answer</td>
<td>32 &gt; = 1</td>
</tr>
<tr>
<td>42</td>
<td>Person 1 Gender</td>
<td style="word-wrap: break-word; white-space: normal;">1, Male | 2, Female | 3, I'd like to consider additional options | 999, Don't know | 777, Decline to answer</td>
<td>32 &gt; = 1</td>
</tr>
<tr>
    <td>43</td>
    <td>Person 1 Gender Additional</td>
    <td style="word-wrap: break-word; white-space: normal;">1, Non-binary | 2, Transgender male | 3, Transgender female | 4, None of these | 999, Don't know | 777, Decline to answer</td>
    <td>32 &gt; = 1</td>
</tr>
<tr>
    <td>44</td>
    <td>Person 1 Relationship to You</td>
    <td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">1, Child | 2, Step Child | 3, Adopted Child | 4, Foster Child | 5, Child-in-Law | 6, Grandchild | 7, Spouse/Partner | 8, Friend/Roommate | 9, Roomer/Boarder | 10, Parent | 16, Step-parent | 11, Parent-in-Law | 12, Grandparent | 13, Sibling | 14, Other Relative | 15, Other Non-relative | 999, Don't know | 777, Decline to answer</span></span></td>
    <td>32 &gt; = 1</td>
</tr>
<tr>
    <td>45</td>
    <td>Person 1 Relationship to CHILD</td>
    <td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-right"><i>Hover for options</i><span class="tooltiptext">1, Parent | 2, Step Parent | 3, Adopted Parent | 4, Foster Parent |5, Full sibling | 6, Half sibling | 7, Non-biologically related sibling | 8, Grandparent | 9, Aunt or Uncle | 10, Cousin | 11, Other Relative | 12, Other Non-relative | 999, Don't know | 777, Decline to answer</span></span></td>
    <td>32 &gt; = 1</td>
</tr>
<tr>
    <td>46</td>
    <td>Person 1 Caregiving</td>
    <td style="word-wrap: break-word; white-space: normal;">1, 1 | ... | 30, 30</td>
    <td>32 &gt; = 1</td>
</tr>
<tr>
    <td>47-151</td>
    <td colspan="2" style="word-wrap: break-word; white-space: normal;"><i>Same set of 6 item questions and branching logic as items 40-46 for Person 1 for Person 2-16 (e.g., Person 2: 47-53: Person 3: 54-60; etc.)</i></td>
    <td></td>
</tr>
<tr>
    <td>152-280</td>
    <td colspan="2" style="word-wrap: break-word; white-space: normal;"><i>Household 2: same item questions and branching logic as Household 1 (item 26 onwards)</i></td>
    <td></td>
</tr>
</tbody>
</table>

#### Income

<table class="compact-table" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th style="width: 1%;">No.</th>
<th style="width: 30%;">Question/Text</th>
<th style="width: 30%;">Response Options/Formula</th>
<th style="width: 5%;">Branching logic</th>
</thead>
<tbody>
<tr style="border-top: 2px solid #c4c2c2ff;">
    <td><strong>281</strong></td>
    <td colspan="2"><strong>Income <i>(section header)</i></strong></td>
    <td></td>
</tr>
<tr>
<td>282</td>
<td style="word-wrap: break-word; white-space: normal;">Which of these categories best describes the TOTAL COMBINED INCOME of the CHILD&rsquo;S HOUSEHOLD(S) for the past 12 months? This should include <span class="tooltip tooltip-top"><i>...</i><span class="tooltiptext" style="width: 400px;">...income (before taxes and deductions) from all sources, wages, rent from properties, social security, disability and/or veteran's benefits, unemployment benefits, workman's compensation, help from relatives (include child payments and alimony), and so on. If the child lives in more than one household, please average the household incomes.</span></span></td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-top"><i>Hover for options</i><span class="tooltiptext" style="width: 400px;">1, Less than $10,000 | 2, $10,000 - $14,999 | 3, $15,000 - $19,999 | 4, $20,000 - $24,999 | 5, $25,000 - $34,999 | 6, $35,000 - $49,999 | 7, $50,000 - $74,999 | 8, $75,000 - $99,999 | 9, $100,000 - $199,999 | 10, $200,000 and greater | 999, Don't know | 777, Decline to answer</span></span></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
