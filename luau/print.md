# print

uhhh... what explanation do you expect?

search for string "current identity is"
```asm
.rdata:0000000006F78F38 aCurrentIdentit db 'Current identity is %d',0
.rdata:0000000006F78F38                                         ; DATA XREF: sub_4267C80+B7↑o
```

first xref

```asm
.text:0000000004267D33                 mov     ebx, dword ptr [rsp+48h+var_28]
.text:0000000004267D37                 lea     rdx, aCurrentIdentit ; "Current identity is %d"
.text:0000000004267D3E                 mov     r8d, ebx
.text:0000000004267D41                 xor     ecx, ecx
.text:0000000004267D43                 call    sub_1CAB4B0
```

sub_1CAB4B0 is the print, well you can decompile it:

```c
    sub_1CAB4B0(a1: 0, a2: "Current identity is %d", (_DWORD)v3);
```

also in same file

```c
  sub_1CAB4B0(a1: 0, a2: "%s %d", v7, (_DWORD)v10);
    sub_1CAB4B0(a1: 0, a2: "Current asset id is %lld", *((_QWORD *)&v10 + 1));
```

just for funnies here's every single string you can get print with, formatted to look like its a staircase just for funnies:

```
%s
%s %d
%s: %s
<no-string>
TestService: %s
  Size/Dim: %.1f
Failed to load %s
HTTP GetAsync: %s
Disconnect from %s
HTTP PostAsync: %s
TeleportService:%s
  RSI: %zu, %.1f kb
  Density(K): %.1f%%
DataModel Loading %s
HTTP RequestAsync: %s
Text scraper error %s
  Density(L+D): %.1f%%
Current identity is %d
Flag %s does not exist
TestService.%s(%d): %s
Server Kick Message: %s
%s 's HSR asset Id is %s
Animation Graph '%s': %s
Current asset id is %lld
Invalid password from %s
Input table missing Order!
Loaded %d shaders in %d ms
  Matrix Size: %zu, %.1f kb
Failed to load video %s: %s
Invalid player to teleport.
The badgeId %lld is invalid
No existing ID found for %s.
Only HTML files are allowed.
getWorldStepId changed %d %d
trying to set locked parent!
  Size/Constraint Count: %.1f
Async Lua function failed: %s
LoadCommonModules no CoreGUI.
Place ID verification failed.
Text scraper failed to start.
TextScraper text too long: %s
exception while signaling: %s
Max DataPing (ms)         : %d
Max RakPing (ms)          : %d
Min DataPing (ms)         : %d
Min RakPing (ms)          : %d
Overall Avg DataPing (ms) : %f
Overall Avg RakPing (ms)  : %f
Overall SD DataPing (ms)  : %f
Overall SD RakPing (ms)   : %f
Ping during join (ms)     : %f
[Tattletale] SENT fullText: %s
-------------------------------
Instance '%s' is not predicted.
AnalyticsService: %s event fired.
AnalyticsService: Invalid status.
Font family %s failed to load: %s
Invalid BrowserService Command %s
[Tattletale] BLOCKED fullText: %s
%s 's HSR data string length is %d
Text scraper successfully started.
MouseIcon can't be set for plugins.
Error fetching player membership: %s
SocialService:OnCallInviteInvoked %s
Collision group name cannot be empty.
Invalid Asset identifier or not found
Server Kick Message: %s; Metadata: %s
Chat message from unknown Player %s %s
Path2D parent rectangle has zero area.
SolverRigidBody Created, new Count: %d
Unable to set %s name to empty string.
AnalyticsService: Ignoring empty event.
Key %s not found in map of player data.
Maximum re-entrancy depth (%i) exceeded
%s: Config value not found for key "%s".
GetCountryRegionForPlayerAsync failed %s
Invalid state passed to GetStateEnabled.
Invalid state passed to SetStateEnabled.
SolverRigidBody Destroyed, new Count: %d
failed to setup input devices because %i
%s: Testing value not found for key "%s".
Error sending TextChatService message: %s
SolidModel SmoothingAngle compute failed.
compileLuaPackages cannot compile scripts
At most %d videos can play simultaneously.
Exponential deferred event growth detected
HumanoidRigDescription is not enabled yet.
Input table contained an invalid asset id!
FingerIndex is expected in the range [1,%d]
Input table  contained an invalid asset id!
SetTeleportGui passed a restricted instance
Unparenting existing styles in SetStyles().
AudioContent does not support opaque content
MarketplaceService:OpenShop: player is null.
Sorry, NotificationService is currently off.
SoundService.ListenerType is not enabled yet
UnequipTools could not find Player backpack!
AudioEmitter.PositionType is not enabled yet.
Failed to upload cage mesh: not in data model
Instance %s should have folders for %s and %s
Instance %s should reference a Decal Instance
R15 Rig Validation: missing required label %d
TileSize must have non-zero width and height.
AudioListener.PositionType is not enabled yet.
Error fetching MarketplaceService receipts: %s
Input contained a badly formed sub data table!
SoundService.ListenerCFrame is not enabled yet
SoundService.ListenerObject is not enabled yet
TextScraper added %zu new entries to table %s.
AnalyticsService: Event field %s is invalid. %s
Asset id %lld should have folders for %s and %s
Asset id %lld should reference a Decal Instance
ClipsDescendants is always true on CanvasGroup.
Keyframe ['%f'] INVALID weight for '%s' => '%f'
Removed invalid attribute '%s' from instance %s
We already gave out badgeId=%lld to userId=%lld
distance: %f, gain factor: %f, spread angle: %f
AnalyticsService: You have sent too many events.
ControlState: ignoring malformed schema for '%s'
Custom layer cannot be set for Air or Water slot
Failed to find awardedCount in badge statistics.
Input table contained an invalid accessory type!
Native code generation of script %s failed:  %s.
R15 Rig Validation: missing required name '%.*s'
Unable to add SDL controller mappings because %s
VideoContent does not support opaque content yet
no native scripts found or compiled successfully
Application::openUrlByCommand, invalid command %s
Failed to load animation with sanitized ID %s: %s
Sit : param is not a Humanoid or humanoid is dead
Text scraper failed to start - Missing DataModel.
WrapDefomer SkinningTransfer Error for '%s': "%s"
Video is using a resolution that is not supported.
compileModuleFolderFromPath cannot compile scripts
AnalyticsService: instance must be a Player object.
Can't debug script %s because debugging is disabled
Collision group name length cannot exceed %zu chars
Failed to find statistics in GetBadgeInfo response.
Failed to resume delayed thread: out of stack space
Failed to resume waiting thread: out of stack space
Input table skipped due to invalid or missing data!
ReflectionService:GetEventsOfClass() is not enabled
TestService: Tests failed to complete in %g seconds
Text scraper failed to start - startService failed.
%s: Testing value type %s for key %s is unsupported.
Dropping received physics update, part %s is unknown
Instance %s should reference a Accoutrement Instance
Video files without video streams are not supported.
Failed to add material layer, max layer count reached
Failed to find winRatePercentage in badge statistics.
GenerateTable operation invoked outside of Edit mode!
Players::onRemoteSysStats disconnect not in the clist
Asset id %lld should reference a Accoutrement Instance
GetFriendsOnline only returns a maximum of 200 friends
Setting GuiService.SelectedObject to invalid GuiObject
Cannot change SolidModel RenderFidelity during Run-Time
Failed to find pastDayAwardedCount in badge statistics.
Instance %s should reference a Folder Instance named %s
LocalizationService text scraper stopped. Processing...
Maximum event re-entrancy depth (%d) exceeded for %s.%s
========================================================
Set humanoidState came from ISR on an unexpected target.
Skip coverage stats because script is missing (name: %s)
The player with userId=%lld is not present at the moment
%s: Set testing value can only be called from the server.
AnalyticsService can only be executed on the game server.
Asset id %lld should reference a Folder Instance named %s
Attempt to connect failed: Passed value is not a function
Failed to register temporary mesh data, no data provided.
Last Known RakNet Time (roundtrip)               :    %d 
Last Known Remote App Recv' to App Read Time     :    %d 
Last Known Remote RakNet Recv' to App Recv' Time :    %d 
Local App Read to App Process Time               :    %d 
Local App Recv' to App Read Time                 :    %d 
Local DataPing Queue To Serialization Time       :    %d 
Local RakNet BCS Queue Time                      :    %d 
Local RakNet Recv' to App Recv' Time             :    %d 
Remote DataPing Read to PingBack Queue Time      :    %d 
Remote DataPingBack Queue To Serialization Time  :    %d 
Remote Last Known RakNet BSC Queue Time          :    %d 
debug.profileEnd() - No active profile annotation. At: %s
ApplyProfileConfiguration failed: could not parse response
Custom layer index cannot be reset, index is out of bounds
Error occurred while calling TextChannel.DisplayBubble: %s
%s: Clear testing value can only be called from the server.
'%s' is a reserved MaterialVariant name and cannot be used.
Failed to load %s. PBR textures may not be visible in game.
Instance %s should reference a CharacterAppearance Instance
Character cannot be changed as Player (%s) is being removed.
Error applying accessory, unknown asset type for instance %s
GetPartBoundsInRadius: Clamping out-of-bounds radius to 0-%f
Hidden Surface Removal data for %s %s is invalid, reason: %s
No cage data exists for %s. TemporaryCageMeshId was not set.
TestService: Run completed, tests: %u, warns: %u, errors: %u
Trying to get rotation data on a device without a gyroscope.
can't set character to %s, only Models or Parts are allowed!
============= UNREL DATA PING BREAK DOWN (in ms) ============
Asset id %lld should reference a CharacterAppearance Instance
AssetService:CreateEditableMesh: Unknown option parameter: %s
Client::OnReceive error while trying to decompress packet: %s
HumanoidDescription:SetAccessories Input table missing Order!
Invalid mesh collision data - reverting to box collisions: %s
Multiple StyleLinks under %s may result in undefined behavior
No cage data exists for %s. TemporaryReferenceId was not set.
RemoteEvent::processRemoteEvent: ignore a remote call from %d
AnimationRigData: Max string size of %d exceeded. Cannot Save.
AssetService:CreateEditableImage: Unknown option parameter: %s
ChatService::serverToClientFilterMessageHandler invalid player
ContextActionService::CallFunction does have a function for %s
Error in HapticService:SetMotor no values found for vibration.
Error occurred while calling TextChannel.OnIncomingMessage: %s
Error occurred while calling TextChatService.OnBubbleAdded: %s
Hidden Surface Removal data generated for %s %s, version is %u
PromptCreateOutfit failed: Unexpected error, success was false
Trying to get gravity data on a device without a accelerometer.
Types of values, %s and %s, do not match. Returning first value
%s: SortOrder.Custom is deprecated, please switch to LayoutOrder
An X axis already exists in the hierarchy for this RotationCurve
An X axis already exists in the hierarchy for this Vector3 Curve
EditableImage:DrawImageTransformed: Unknown option parameter: %s
RemoteFunction::processRemoteEvent: ignore a remote call from %d
AnimationRigData: Max component size of %d exceeded. Cannot Save.
Batch Thumbnail invalid thumbnail type for %s: Valid types are %s
DigitsRigDescription is missing some data for finger %d, skipping
Dropping received physics update, part %s is not in the workspace
MarketplaceService:OpenShop: cannot open shop for a guest player.
ModuleScript %s detected as malicious.  Script has been disabled.
R15 Rig Validation: NaN/Inf in CFrames (pre=%s post=%s xforms=%s)
Sorry, NotificationService only works on touch devices currently.
Waiting for server to authenticate the placeID before spawning...
AssetService:CreateEditableMeshAsync: Unknown option parameter: %s
Error occurred while calling TextChannel.ShouldDeliverCallback: %s
Error occurred while calling TextChatService.OnChatWindowAdded: %s
Error occurred while calling TextChatService.OnIncomingMessage: %s
MaterialVariant '%s' uses a reserved name and cannot be activated.
R15 Rig Validation: NaN/Inf in joint %zu (pre=%s post=%s tpose=%s)
StarterPlayerScripts must be a child of StarterPlayer.  %s is not.
%s.%s has local asset '%s'. Local asset is not supported in client.
AssetService:CreateSurfaceAppearance: Unknown content parameter: %s
Base material (%s) is not currently supported for MaterialVariants.
RoMarkError: Attempted to disconnect but found no oldest replicator
Cannot start client script '%s' (lacking capability RunClientScript)
Cannot start server script '%s' (lacking capability RunServerScript)
LDL program %llu, Bundles: %zu, Dim(K): %d, Size(K): %zu, Flops: %zu
Trying to get acceleration data on a device without a accelerometer.
Trying to listen to rotation events on a device without a gyroscope.
%s.%s has invalid texture '%s'. TexturePack only supports rbxassetid.
AvatarEditorService unexpected value for %s when converting to string
Duplicate joint name detected! Animation might not play correctly. %s
Failed to evaluate style value function for property '%s' in '%s': %s
Ignoring ScaleTo(NaN) call, check your code for divide by zero errors
More than one Cloud instance in workspace, first enabled one is used.
AnalyticsService:GetPlayerSegmentsAsync parse failed responseBytes=%zu
AnimationRigData: component size %u larger than available read buffer.
ChatInputBarConfiguration.TextBox should be a descendant of PlayerGui.
MarketplaceService:OpenShop() API failed: Module initialization error.
==== Total Unrel DataPing Estimate from above %d vs Measured %d =======
LocalizationService: CoreScriptLocalization missing from DataModelPatch
{ t1+...+tn (ms) , t1^2+...+tn^2 (ms^2) , n }["%s"]={ %lf , %lf , %zu }
Cloud instance must exist under Terrain node in workspace to be visible.
TestService: on %s: waiting a total of %0.2f seconds for the test to end
AddAcessory failed: Accessory is already being worn by another character.
Cannot apply UISizeConstraint with invalid constraints MinSize > MaxSize.
Children removed from StarterPlayerScripts not parented to StarterPlayer.
PromptCreateOutfit failed: Unexpected error, invalid type of errors value
Batch Thumbnail invalid id for %s: Id must be greater than 0. Got id: %lld
ContextActionService could not find the function passed in, doing nothing.
SetRoll can only be used on Camera objects with a CameraType of Scriptable
GuiService:AddSelectionParent for group name %s: parent is not a GuiObject.
StyleDerive %s is set to %s, which creates a circular derive loop. Ignoring
JointsService is deprecated, but an instance was added to JointsService: %s 
NotificationService:ScheduleNotification must be called from a local script!
PrivateServerId cannot be checked on the client, please check on the server.
Remote event invocation queue data rate limit reached on %s.%s.  (%d errors)
Sorry, badges can only be tested if they are disabled on Roblox game servers
Trying to listen to acceleration events on a device without a accelerometer.
AnimationRigData: Max string size of %d exceeded. Rig may not load correctly.
Batch Thumbnail invalid thumbnail size for %s: Valid sizes for type %s are %s
Error occurred while calling TextChatService.invokeChannelDeliverCallback: %s
Native code generation of script %s failed:  %s.  Script will be interpreted.
No AnimationPose returned by callback from RegisterEvaluationParallelCallback
ScrollingFrame.ScrollBarThickness set to negative value, clamping value to 0.
A custom head instance should contain the appropriate Attachments as children.
Mesh %s failed to load because it has not been moderated yet. Retrying soon...
ContentProvider:getContent() in fetching HSR data does not have response for %s
AnimationRigData: Max component size of %d exceeded. Rig may not load correctly.
Cancelling remaining scheduled operations due to shutdown deadline being reached
"%s.%s" is not a FloatCurve channel in CurveAnimation: %s, ignoring this control.
Cannot do linear interpolation for type  %s. Doing constant interpolation instead
HSR data for %s has not uploaded as hsrId, please publish the place or the model.
PrivateServerOwnerId cannot be checked on the client, please check on the server.
Unexpected value in AvatarEditorService:SearchCatalog result: expected ValueTable
CanvasGroup: %u group(s) using individual draw fallback (OOM or allocation failure)
The provided character model is null or the instance is not under a character model
Cannot reparent '%s' to '%s' because this would create a circular package dependency
UserInputSerice.IsMouseButtonPressed - UserInputType provided is not a mouse button.
AvatarSettings:Publish() failed!\n- statusCode: %d\n- statusMessage: %s\n- body: %s\n
AnalyticsService:GetPlayerSegmentsAsync HTTP failed status=%d err=%s responseBytes=%zu
Cannot set GamepadService.EnableGamepadCursor on %s because it is outside the viewport
Failed to create EditableMesh that was requested due to reaching memory budget limits.
Hidden Surface Removal AssetId for %s does not exist, please publish your place again.
Instance %s should reference an Accoutrement Instance which has a WrapLayer descendent
Remote event invocation %s for %s; did you forget to implement %s? (%u events dropped)
Failed to create EditableImage that was requested due to reaching memory budget limits.
HSR data for %s %s does not have an asset, please publish the place or the model again.
ValueCurve::setKeys -- Type of Value %s does not match existing keys. Key not inserted.
A FloatCurve child named %s already exists in the hierarchy for this CompositeValueCurve
Asset id %lld should reference an Accoutrement Instance which has a WrapLayer descendent
Cannot set GamepadService.EnableGamepadCursor on %s because it must have visible == true
LocalizationService: CoreScriptLocalization in DataModelPatch is not a LocalizationTable
Tool:Activate() called from script when tool is not equipped. Tool will not be activated.
ValueCurve::insertKey -- Type of Value %s does not match existing keys. Key not inserted.
ModelStreamingMode cannot be changed from a LocalScript. Model behavior will be undefined.
PathfindingModifier '%s' has property 'Label' set to '%s', which will be treated as '%s'. 
Remote function invocation %s for %s; did you forget to implement %s ? (%u events dropped)
EditableMesh is not accessible. Go to the Security Tab in Game Settings to enable this API.
EditableImage is not accessible. Go to the Security Tab in Game Settings to enable this API.
Failed to create empty EditableMesh that was requested due to reaching memory budget limits.
Instance outside of DataModel; could not read property Workspace.MeshPartHeadsAndAccessories
More than one [Motor6D / AnimationConstraint] driving part %s. Using %s and disregarding %s.
Failed to create empty EditableImage that was requested due to reaching memory budget limits.
Tool:Deactivate() called from script when tool is not equipped. Tool will not be deactivated.
Instance %s should reference a single MeshPart or DataModelMesh, or have folders for %s and %s
Asset id %lld should reference a single MeshPart or DataModelMesh, or have folders for %s and %s
Failed to add navigation area '%s'.  Only %d navigation areas per navigation tile can be stored.
Player::LoadCharacterWithHumanoidDescription() humanoidDescription contains duplicate assets: %s
RunService:UnbindFromRenderStep removed different functions with same reference name %s %i times.
GuiService:AddSelectionTuple already has selection group with name %s, overwriting selection group.
smoothSkinning: length of the input skinning vector %d does not equal to the number of vertices %d.
GuiService:AddSelectionParent already has selection group with name %s, overwriting selection group.
Hidden Surface Removal does not generate correct result with mesh id %s, cage id %s, reference id %s
LocalizationTable:SetEntries dropped %zu entries with duplicate (key) or (key,source,context) from %s
Passing Character instance into teleport functions is deprecated. Please use Player instance instead.
Cannot set CursorPosition on a TextBox that is reserved for TextChatService.ChatInputBarConfiguration.
Cannot set SelectionStart on a TextBox that is reserved for TextChatService.ChatInputBarConfiguration.
Workspace.MeshPartHeadsAndAccessories must be enabled for layered clothing to work in your experience.
Cannot set GamepadService.EnableGamepadCursor on %s because it is a child of a billboard or surface gui
Cannot set GamepadService.EnableGamepadCursor on %s because it is outside of the Scrolling Frame window
Server Error 500. Permissions to asset %lld cannot be retrieved at this time. Please check again later.
smoothSkinning: length of the input applyToVerts vector %d does not equal to the number of vertices %d.
Cannot set GamepadService.EnableGamepadCursor on %s because it must have all parents with visible == true
TextScraper found no new text that wasn't already in a table. No new table or new entries were generated.
Unable to generate '%s' due to some of the textures being unavailable. Change a TextureId property to retry.
AnimationGraph Server Authority: parameter '%s' will not replicate; the graph exceeds replication limits (%s).
Cannot set GamepadService.EnableGamepadCursor on %s because it is a child of a ScreenGui with enabled == false
ValueCurve::setKeys -- Type of all keys is not the same. First key type is %s but subsequent key is of type %s
Player::LoadCharacterWithHumanoidDescription() HumanoidDescription has BodyPartDescriptions with the same BodyPart.
Failed to play animation: %s. AnimationTrack limit of %d tracks exceeded for '%s', new animations will not be played.
AccessoryBlob requires entries to have IsLayered set to true (or don't set IsLayered, and default value will be used)!
Warning: `%s` property `%s` is overridden by a StyleRule. Use Instance:GetStyled(property) to get the styled property value.
AssetService:CreateEditableImageAsync: Failed to create EditableImage that was requested due to reaching memory budget limits.
IsLayered is required to be true for entries where order is specified (or don't set IsLayered, and default value will be used)!
IsLayered is required to be false for entries where order is not specified (or don't set IsLayered, and default value will be used)!
R15 Rig Validation: size check failed (labels=%zu expected=%zu children=%zu names=%zu joints=%zu pre=%zu post=%zu xforms=%zu adf=%d)
clientInstanceQuota %d, packet in queue %d, predictedTotalInstanceProcessTime %f, avgStreamDataReadTime %f, avgInstancesPerStreamData %f
rbxgameasset urls are currently not supported on %s.%s. Use the image asset's rbxassetid (can be copied from the Toolbox or Game Explorer).
MarketplaceService:OpenShop: called from a local script, but not called on a local player. Local scripts can only open the shop for the local player.
MarketplaceService:PromptNativePurchase called from a local script, but not called on a local player. Local scripts can only prompt the local player.
MarketplaceService:PromptNativePurchaseWithPaymentSessionId called from a local script, but not called on a local player. Local scripts can only prompt the local player.
```
R15 Rig Validation: failed (tooMany=%s componentMismatch=%s transformsInconsistent=%s labels=%zu names=%zu parents=%zu pre=%zu post=%zu tpose=%zu maxFlag=%d Count-1=%zu)
R15 Rig Validation: failed (tooMany=%s componentMismatch=%s transformsInconsistent=%s labels=%zu children=%zu names=%zu joints=%zu pre=%zu post=%zu xforms=%zu maxFlag=%d Count-1=%zu)
LDLProgram Id: %d, Dim: %d, Ext Dim: %d, Ops: %.0f k, L Height Max / Ave: %d / %.0f, GigOps/s: %.2f / %.2f, Flops/Dim: %.0f, Initialization: %.2f / %.2f us, Elimination: %.2f / %.2f us, Total: %.2f / %.2f us
%s: UseWorkspaceCollisionGroups is true, so this WorldModel's own collision groups are not the ones used for its simulation. If you meant to access or change the simulated groups, set UseWorkspaceCollisionGroups to false or edit them on the Workspace.
