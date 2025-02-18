
下面是每个 OSC 路径的中文注释说明，这些路径用于控制 Resolume 中合成（Composition）、图层（Layer）、剪辑（Clip）等各个模块的参数和行为。

//COMPOSITION （合成控制）
/composition/connectnextcolumn
连接到下一个列。

/composition/connectprevcolumn
连接到前一个列。

/composition/connectspecificcolumn
连接到指定的列。

/composition/audio/pan
设置合成整体的音频声像（左右平衡）。

/composition/audio/volume
设置合成整体的音量。

/composition/bypassed
启用或禁用合成（旁路效果）。

/composition/direction
设置合成的播放方向。

/composition/disconnectall
断开合成中所有的连接。

/composition/master
指定或切换合成的主控状态。

/composition/name
设置或获取合成的名称。

/composition/selectnextdeck
选择下一个 Deck（演奏台）。

/composition/selectprevdeck
选择上一个 Deck。

/composition/selectspecificdeck
选择指定的 Deck。

/composition/speed
调整合成的播放速度。

/composition/video/effects/transform/anchorx
设置合成视频变换效果的 X 轴锚点。

/composition/video/effects/transform/anchory
设置合成视频变换效果的 Y 轴锚点。

/composition/video/effects/transform/anchorz
设置合成视频变换效果的 Z 轴锚点。

/composition/video/effects/transform/bypassed
禁用或启用视频变换效果。

/composition/video/effects/transform/positionx
设置视频变换效果的位置（X 坐标）。

/composition/video/effects/transform/positiony
设置视频变换效果的位置（Y 坐标）。

/composition/video/effects/transform/rotationx
设置视频在 X 轴上的旋转角度。

/composition/video/effects/transform/rotationy
设置视频在 Y 轴上的旋转角度。

/composition/video/effects/transform/rotationz
设置视频在 Z 轴上的旋转角度。

/composition/video/effects/transform/scale
设置视频变换效果的整体缩放比例。

/composition/video/effects/transform/scaleh
设置视频变换效果的垂直缩放比例。

/composition/video/effects/transform/scalew
设置视频变换效果的水平缩放比例。

/composition/video/height
设置合成视频的高度。

/composition/video/opacity
设置合成视频的透明度。

/composition/video/width
设置合成视频的宽度。

/composition/dashboard/link1 ～ link8
控制合成仪表板上预设的 8 个链接（可用于快速触发或切换功能）。

//LAYER （图层控制，示例为第 1 层）
/composition/layers/1/audio/pan
设置第 1 层音频的声像平衡。

/composition/layers/1/audio/volume
设置第 1 层的音量。

/composition/layers/1/autopilot
启用或禁用第 1 层的自动播放模式。

/composition/layers/1/bypassed
启用或禁用第 1 层（旁路该层的效果）。

/composition/layers/1/clear
清除第 1 层中的所有内容。

/composition/layers/1/connectnextclip
连接到第 1 层的下一个剪辑。

/composition/layers/1/connectprevclip
连接到第 1 层的上一个剪辑。

/composition/layers/1/connectspecificclip
连接到第 1 层中指定的剪辑。

/composition/layers/1/crossfadergroup
设置第 1 层所属的交叉淡化组。

/composition/layers/1/dashboard/link1 ～ link8
控制第 1 层仪表板上预设的 8 个链接。

/composition/layers/1/direction
设置或获取第 1 层的播放方向。

/composition/layers/1/faderstart
设置第 1 层渐变/混合起始值。

/composition/layers/1/ignorecolumntrigger
设置第 1 层是否忽略列触发事件。

/composition/layers/1/maskmode
设置第 1 层的遮罩模式。

/composition/layers/1/master
将第 1 层设为主层，或控制该层的主控状态。

/composition/layers/1/name
设置或获取第 1 层的名称。

/composition/layers/1/playmode
设置第 1 层的播放模式（如循环、触发、单次播放等）。

/composition/layers/1/position
设置第 1 层在堆叠中的位置。

/composition/layers/1/select
选择第 1 层。

/composition/layers/1/selected
获取第 1 层是否处于选中状态。

/composition/layers/1/smpte1quickselect
快速选择与 SMPTE 1 时间码相关的第 1 层设置。

/composition/layers/1/smpte2quickselect
快速选择与 SMPTE 2 时间码相关的第 1 层设置。

/composition/layers/1/solo
将第 1 层设为独奏状态（屏蔽其他层）。

/composition/layers/1/speed
设置第 1 层的播放速度。

/composition/layers/1/transition/duration
设置第 1 层过渡效果的持续时间。

/composition/layers/1/triggerfirstcliponload
设置在加载时是否自动触发第 1 层的第一个剪辑。

/composition/layers/1/video/autosize
设置第 1 层视频是否自动调整大小以适应窗口。

/composition/layers/1/video/effects/transform/anchorx
设置第 1 层视频变换效果的 X 轴锚点。

/composition/layers/1/video/effects/transform/anchory
设置第 1 层视频变换效果的 Y 轴锚点。

/composition/layers/1/video/effects/transform/anchorz
设置第 1 层视频变换效果的 Z 轴锚点。

/composition/layers/1/video/effects/transform/positionx
设置第 1 层视频效果的位置（X 坐标）。

/composition/layers/1/video/effects/transform/positiony
设置第 1 层视频效果的位置（Y 坐标）。

/composition/layers/1/video/effects/transform/rotationx
设置第 1 层视频在 X 轴上的旋转角度。

/composition/layers/1/video/effects/transform/rotationy
设置第 1 层视频在 Y 轴上的旋转角度。

/composition/layers/1/video/effects/transform/rotationz
设置第 1 层视频在 Z 轴上的旋转角度。

/composition/layers/1/video/effects/transform/scale
设置第 1 层视频整体的缩放比例。

/composition/layers/1/video/effects/transform/scaleh
设置第 1 层视频的垂直缩放比例。

/composition/layers/1/video/effects/transform/scalew
设置第 1 层视频的水平缩放比例。

/composition/layers/1/video/height
设置第 1 层视频的高度。

/composition/layers/1/video/mixer/blendmode
设置第 1 层视频的混合模式。

/composition/layers/1/video/opacity
设置第 1 层视频的透明度。

/composition/layers/1/video/transition/mixer/blendmode
设置第 1 层视频在过渡时的混合模式。

/composition/layers/1/video/width
设置第 1 层视频的宽度。

//CLIP （剪辑控制，示例为第 1 层中的第 1 个剪辑）
/composition/layers/1/clips/1/autopilot
设置剪辑的自动播放模式。

/composition/layers/1/clips/1/beatsnap
启用剪辑的节拍对齐（Beat Snap）功能。

/composition/layers/1/clips/1/cliptarget
指定剪辑的目标输出或连接对象。

/composition/layers/1/clips/1/cliptriggerstyle
设置剪辑触发时的行为样式（如瞬间触发或渐变切换）。

/composition/layers/1/clips/1/connect
连接剪辑（触发或关联至其他剪辑）。

/composition/layers/1/clips/1/connected
获取剪辑当前的连接状态。

/composition/layers/1/clips/1/dashboard/link1 ～ link8
控制剪辑仪表板上预设的 8 个链接。

/composition/layers/1/clips/1/faderstart
设置剪辑的起始渐变值。

/composition/layers/1/clips/1/ignorecolumntrigger
设置剪辑是否忽略列触发。

/composition/layers/1/clips/1/name
设置或获取剪辑的名称。

/composition/layers/1/clips/1/select
选择该剪辑。

/composition/layers/1/clips/1/selected
获取该剪辑是否处于选中状态。

/composition/layers/1/clips/1/transporttype
设置剪辑的传输类型（播放模式、触发模式等）。

/composition/layers/1/clips/1/transport/position
设置或获取剪辑的播放位置。

/composition/layers/1/clips/1/transport/position/behaviour/speed
设置播放位置变化时的速度行为。

/composition/layers/1/clips/1/transport/position/behaviour/dividetwo
将播放位置的变动速率除以 2。

/composition/layers/1/clips/1/transport/position/behaviour/multiplytwo
将播放位置的变动速率乘以 2。

/composition/layers/1/clips/1/transport/position/behaviour/syncmode
设置播放位置的同步模式。

/composition/layers/1/clips/1/transport/position/behaviour/playdirection
设置剪辑播放时的方向行为。

/composition/layers/1/clips/1/transport/position/behaviour/playmode
设置剪辑的播放模式（例如单次、循环）。

/composition/layers/1/clips/1/transport/position/behaviour/playmodeaway
设置播放模式的偏移或特殊行为。

/composition/layers/1/clips/1/video/mixer/blendmode
设置剪辑视频的混合模式。

/composition/layers/1/clips/1/video/opacity
设置剪辑视频的透明度。

/composition/layers/1/clips/1/video/width
设置剪辑视频的宽度。

/composition/layers/1/clips/1/video/height
设置剪辑视频的高度。

/composition/layers/1/clips/1/video/scaletofit
使剪辑视频按比例自适应窗口尺寸。

/composition/layers/1/clips/1/video/rscale
调整剪辑视频红色通道的缩放比例。

/composition/layers/1/clips/1/video/gscale
调整剪辑视频绿色通道的缩放比例。

/composition/layers/1/clips/1/video/bscale
调整剪辑视频蓝色通道的缩放比例。

/composition/layers/1/clips/1/video/ascale
调整剪辑视频 Alpha 通道的缩放比例。

/composition/layers/1/clips/1/transport/cuepoints/setparams/set1
设置剪辑第 1 个 Cue 点的参数。

/composition/layers/1/clips/1/transport/cuepoints/jumpparams/jump1
设置剪辑第 1 个 Cue 点的跳转参数。

/composition/layers/1/clips/1/transport/cuepoints/setparams/set2
设置剪辑第 2 个 Cue 点的参数。

/composition/layers/1/clips/1/transport/cuepoints/jumpparams/jump2
设置剪辑第 2 个 Cue 点的跳转参数。

/composition/layers/1/clips/1/transport/cuepoints/setparams/set3
设置剪辑第 3 个 Cue 点的参数。

/composition/layers/1/clips/1/transport/cuepoints/jumpparams/jump3
设置剪辑第 3 个 Cue 点的跳转参数。

/composition/layers/1/clips/1/transport/cuepoints/setparams/set4
设置剪辑第 4 个 Cue 点的参数。

/composition/layers/1/clips/1/transport/cuepoints/jumpparams/jump4
设置剪辑第 4 个 Cue 点的跳转参数。

/composition/layers/1/clips/1/transport/cuepoints/setparams/set5
设置剪辑第 5 个 Cue 点的参数。

/composition/layers/1/clips/1/transport/cuepoints/jumpparams/jump5
设置剪辑第 5 个 Cue 点的跳转参数。

/composition/layers/1/clips/1/transport/cuepoints/setparams/set6
设置剪辑第 6 个 Cue 点的参数。

/composition/layers/1/clips/1/transport/cuepoints/jumpparams/jump6
设置剪辑第 6 个 Cue 点的跳转参数。

/composition/layers/1/clips/1/video/effects/transform/anchorx
设置剪辑视频变换效果的 X 轴锚点。

/composition/layers/1/clips/1/video/effects/transform/anchory
设置剪辑视频变换效果的 Y 轴锚点。

/composition/layers/1/clips/1/video/effects/transform/anchorz
设置剪辑视频变换效果的 Z 轴锚点。

/composition/layers/1/clips/1/video/effects/transform/positionx
设置剪辑视频效果的位置（X 坐标）。

/composition/layers/1/clips/1/video/effects/transform/positiony
设置剪辑视频效果的位置（Y 坐标）。

/composition/layers/1/clips/1/video/effects/transform/rotationx
设置剪辑视频在 X 轴上的旋转角度。

/composition/layers/1/clips/1/video/effects/transform/rotationy
设置剪辑视频在 Y 轴上的旋转角度。

/composition/layers/1/clips/1/video/effects/transform/rotationz
设置剪辑视频在 Z 轴上的旋转角度。

/composition/layers/1/clips/1/video/effects/transform/scale
设置剪辑视频整体的缩放比例。

/composition/layers/1/clips/1/video/effects/transform/scaleh
设置剪辑视频的垂直缩放比例。

/composition/layers/1/clips/1/video/effects/transform/scalew
设置剪辑视频的水平缩放比例。

//COLUMNS （列控制，示例为第 1 列）
/composition/columns/1/connect
连接第 1 列。

/composition/columns/1/name
设置或获取第 1 列的名称。

/composition/columns/1/selected
设置或获取第 1 列的选中状态。

//CROSSFADER （交叉淡化控制）
/composition/crossfader/behaviour
设置交叉淡化的行为模式。

/composition/crossfader/curve
设置交叉淡化时的曲线形状。

/composition/crossfader/phase
设置交叉淡化的相位（偏移）。

/composition/crossfader/sidea
设置或获取交叉淡化 A 侧的值。

/composition/crossfader/sideb
设置或获取交叉淡化 B 侧的值。

/composition/crossfader/video/mixer/blendmode
设置交叉淡化视频的混合模式。

//DECKS （Deck 控制）
/composition/decks/1/name
设置或获取第 1 个 Deck 的名称。

/composition/decks/1/select
选择第 1 个 Deck。

//BPM （节奏/速度控制）
/composition/tempocontroller/metronome
启用或禁用节拍器功能。

/composition/tempocontroller/pause
暂停或恢复节奏控制。

/composition/tempocontroller/resync
重新同步节奏。

/composition/tempocontroller/tempo
设置或获取当前的 BPM（节奏速度）。

/composition/tempocontroller/tempodec
降低 BPM 数值。

/composition/tempocontroller/tempodividetwo
将 BPM 数值除以 2。

/composition/tempocontroller/tempoinc
提高 BPM 数值。

/composition/tempocontroller/tempomultiplytwo
将 BPM 数值乘以 2。

/composition/tempocontroller/tempopull
以“拉”的方式调整 BPM（降低节奏）。

/composition/tempocontroller/tempopush
以“推”的方式调整 BPM（提高节奏）。

/composition/tempocontroller/tempotap
通过敲击节拍来设置 BPM。

//SMPTE （时间码控制）
/smptecontroller/smpte1offset
设置 SMPTE 1 时间码的偏移量。

/smptecontroller/smpte2offset
设置 SMPTE 2 时间码的偏移量。

//CLIP SCROLL BAR （剪辑滚动条控制）
/application/ui/clipsscrollhorizontal
控制用户界面中剪辑区域的水平滚动条。

/application/ui/clipsscrollvertical
控制用户界面中剪辑区域的垂直滚动条。

//GLOBAL FFT GAIN （全局 FFT 输入增益）
/audiodevicemanager/params/fftinputgain
设置音频设备 FFT 输入的全局增益。
//RECORD （录制控制）
/composition/recorder/record
开始或停止录制合成输出。
